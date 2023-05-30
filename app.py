from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = '1234'

# 데이터베이스 연결
databass = 'data/board.db'
conn = sqlite3.connect(databass)
c = conn.cursor()

# 게시판 테이블 생성
c.execute('''CREATE TABLE IF NOT EXISTS board
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT NOT NULL,
              content TEXT NOT NULL,
              author TEXT NOT NULL,
              date TEXT NOT NULL)''')

# 공지사항 테이블 생성
c.execute('''CREATE TABLE IF NOT EXISTS notice
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT NOT NULL,
              content TEXT NOT NULL,
              author TEXT NOT NULL,
              date TEXT NOT NULL)''')

# 사용자 테이블 생성
c.execute('''CREATE TABLE IF NOT EXISTS user
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL,
              password TEXT NOT NULL,
              is_admin INTEGER NOT NULL)''')

# 어드민 계정 생성
#c.execute('''INSERT INTO user (username, password, is_admin) VALUES (?, ?, ?)''', ('admin', 'admin', 1))

# 데이터베이스 연결 종료
conn.commit()
conn.close()

def popupmassage(txt):
    return '<script>alert("'+str(txt)+'");history.go(-1);</script>'

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 게시판 페이지
@app.route('/board')
def board():
    # 게시글 목록 가져오기
    conn = sqlite3.connect(databass)
    c = conn.cursor()
    c.execute('SELECT * FROM board ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return render_template('board.html', rows=rows)

# 게시글 작성 페이지
@app.route('/board/write')
def board_write():
    # 로그인 여부 확인
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('board_write.html')

# 게시글 작성 처리
@app.route('/board/write_process', methods=['POST'])
def board_write_process():
    # 게시글 정보 가져오기
    title = request.form['title']
    content = request.form['content']
    author = request.form['author']
    date = request.form['date']
    # 게시글 저장
    conn = sqlite3.connect(databass)
    c = conn.cursor()
    c.execute('INSERT INTO board (title, content, author, date) VALUES (?, ?, ?, ?)', (title, content, author, date))
    conn.commit()
    conn.close()
    return redirect(url_for('board'))

# 게시글 상세 페이지
@app.route('/board/<int:id>')
def board_detail(id):
    # 게시글 정보 가져오기
    conn = sqlite3.connect(databass)
    c = conn.cursor()
    c.execute('SELECT * FROM board WHERE id = ?', (id,))
    row = c.fetchone()
    conn.close()
    return render_template('board_detail.html', row=row)

# 공지사항 페이지
@app.route('/notice')
def notice():
    # 공지사항 목록 가져오기
    conn = sqlite3.connect(databass)
    c = conn.cursor()
    c.execute('SELECT * FROM notice ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return render_template('notice.html', rows=rows)

# 공지사항 작성 페이지
@app.route('/notice/write')
def notice_write():
    # 어드민 여부 확인
    if 'username' not in session or not session['is_admin']:
        return redirect(url_for('login'))
    return render_template('notice_write.html')

# 공지사항 작성 처리
@app.route('/notice/write_process', methods=['POST'])
def notice_write_process():
    # 어드민 여부 확인
    if 'username' not in session or not session['is_admin']:
        return redirect(url_for('login'))
    # 공지사항 정보 가져오기
    title = request.form['title']
    content = request.form['content']
    author = request.form['author']
    date = request.form['date']
    # 공지사항 저장
    conn = sqlite3.connect(databass)
    c = conn.cursor()
    c.execute('INSERT INTO notice (title, content, author, date) VALUES (?, ?, ?, ?)', (title, content, author, date))
    conn.commit()
    conn.close()
    return redirect(url_for('notice'))

# 공지사항 상세보기 페이지
@app.route('/notice/<int:id>')
def notice_detail(id):
    # 공지사항 정보 가져오기
    conn = sqlite3.connect(databass)
    c = conn.cursor()
    c.execute('SELECT * FROM notice WHERE id = ?', (id,))
    row = c.fetchone()
    conn.close()
    # 공지사항 정보가 없는 경우 404 에러 반환
    if not row:
        return render_template('404.html')
    return render_template('notice_detail.html', row=row)

# 검색 처리
@app.route('/search', methods=['POST'])
def search():
    # 검색어 가져오기
    keyword = request.form['keyword']
    # 게시글 검색
    conn = sqlite3.connect(databass)
    c = conn.cursor()
    c.execute('SELECT * FROM board WHERE title LIKE ? OR content LIKE ?', ('%'+keyword+'%', '%'+keyword+'%'))
    rows = c.fetchall()
    conn.close()
    return render_template('search.html', rows=rows)

# 로그인 페이지
@app.route('/login')
def login():
    return render_template('login.html')

# 로그인 처리
@app.route('/login_process', methods=['POST'])
def login_process():
    # 사용자 정보 가져오기
    username = request.form['username']
    password = request.form['password']
    # 사용자 인증
    try:
        conn = sqlite3.connect(databass)
        c = conn.cursor()
        c.execute('SELECT * FROM user WHERE username = ? AND password = ?', (username, password))
        user = c.fetchone()
        conn.close()
    except:
        return popupmassage('잘못된 정보입니다.')
        #return redirect(url_for('login'))

    if user:
        session['username'] = user[1]
        if user[3] == 1:
            session['is_admin'] = True
            return redirect(url_for('index'))
        else:
            session['is_admin'] = False
            return redirect(url_for('index'))
    else:
        return popupmassage('잘못된 정보입니다.')
        #return redirect(url_for('login'))
    

# 회원가입 페이지
@app.route('/register')
def register():
    return render_template('register.html')

# 회원가입 처리
@app.route('/register_process', methods=['POST'])
def register_process():
    # 사용자 정보 가져오기
    username = request.form['username']
    password = request.form['password']

    # 중복 username 체크
    conn = sqlite3.connect(databass)
    c = conn.cursor()
    c.execute('SELECT * FROM user WHERE username = ?', (username,))
    result = c.fetchone()
    if result:
        conn.close()
        return popupmassage('이미 존재하는 id 입니다.')
        return redirect(url_for('register'))

    # 유효성 검사
    if not username or not password:
        conn.close()
        return popupmassage('모든 항목을 입력해주세요')
        return redirect(url_for('register'))

    # 사용자 등록
    c.execute('INSERT INTO user (username, password, is_admin) VALUES (?, ?, ?)', (username, password, 0))
    conn.commit()
    conn.close()
    return redirect(url_for('login'))


#로그아웃 처리
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('is_admin', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
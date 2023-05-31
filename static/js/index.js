window.addEventListener('load', function () {
    var mainCont = document.querySelector('.mainCont');
    var serveCont = document.querySelector('.serveCont');
    var lNotice = document.querySelector('.lNotice');
    var noticeBox = document.querySelector('.noticeBox');
    var rLunch = document.querySelector('.lLunch');
    var lunchBox = document.querySelector('.lunchBox');

    setTimeout(function () {
        mainCont.classList.add('mainCont-move');
        setTimeout(function () {
            serveCont.classList.add('serveCont-move');
            setTimeout(function () {
                lNotice.classList.add('lNotice-move');
                setTimeout(function () {
                    rLunch.classList.add('lLunch-move');
                    setTimeout(function () {
                        noticeBox.classList.add('noticeBox-move');
                        setTimeout(function () {
                            lunchBox.classList.add('lunchBox-move');
                            
                        }, 100);
                    }, 300);
                }, 100);
            }, 300);
        }, 100);
    }, 1500);
});
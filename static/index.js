window.addEventListener('load', function () {
    var mainCont = document.querySelector('.mainCont');
    var serveCont = document.querySelector('.serveCont');
    var container = document.querySelector('.container');
    var logo = document.querySelector('.logo');
    var bar = document.querySelector('.bar');
    var menuL = document.querySelector('.menuL');
    var menuN = document.querySelector('.menuN');
    var menuC = document.querySelector('.menuC');

    container.classList.add('fade-out');

    setTimeout(function () {
        logo.classList.add('shrink-and-move');
        setTimeout(function () {
            logo.classList.add('logo-move');
            bar.classList.add('bar-move');
            setTimeout(function () {
                menuC.classList.add('menuC-move');
                mainCont.classList.add('mainCont-move');
                setTimeout(function () {
                menuN.classList.add('menuN-move');
                serveCont.classList.add('serveCont-move');
                    setTimeout(function () {
                    menuL.classList.add('menuL-move');
                    }, 100);
                }, 100);
            }, 500);
        }, 500);
    }, 500);
});
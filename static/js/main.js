window.addEventListener('load', function () {
    var curtain = document.querySelector('.curtain');
    var logo = document.querySelector('.logo');
    var bar = document.querySelector('.bar');
    var menuL = document.querySelector('.menuL');
    var menuN = document.querySelector('.menuN');
    var menuC = document.querySelector('.menuC');

    


    curtain.classList.add('fade-out');

    setTimeout(function () {
        logo.classList.add('shrink-and-move');
        setTimeout(function () {
            logo.classList.add('logo-move');
            bar.classList.add('bar-move');
            setTimeout(function () {
                menuC.classList.add('menuC-move');
                setTimeout(function () {
                    menuN.classList.add('menuN-move');
                    setTimeout(function () {
                        menuL.classList.add('menuL-move');
                    }, 100);
                }, 100);
            }, 500);
        }, 500);
    }, 500);
});
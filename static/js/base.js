window.addEventListener('load', function () {
    var curtain = document.querySelector('.curtain');
    
    curtain.classList.add('fade-in');
    setTimeout(function () {
        curtain.classList.add('fade-out');
    }, 600);
    
});
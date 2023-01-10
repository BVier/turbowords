// $('.footer').on(click, '.reload', reloadWord)

function reloadWord(){
    word = document.querySelector('.word');
    word.classList.remove('animate');
    // void word.offsetWidth;
    word.classList.add('animate');
    // word.style.animationPlayState="paused";  
    // word.style.animationPlayState="running";
}
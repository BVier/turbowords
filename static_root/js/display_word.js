function reloadWord(){
    word = document.querySelector('.word');
    word.classList.remove('animate');
    void word.offsetWidth;
    word.classList.add('animate');
}
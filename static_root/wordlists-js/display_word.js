$('.footer').on(click, '.reload', reloadWord)

function reloadWord(){
    word = $('.word')
    word.classList.remove('animate');
    void word.offsetWidth;
    word.classList.add('animate');
}
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from random import shuffle

# Create your views here.


def index(request):
    wordlist_list = Wordlist.objects.order_by('-name')[:5]
    for wordlist in wordlist_list:
        wordlist.count_words = len(wordlist.words.splitlines())
    context = {'latest_wordlist_list': wordlist_list}
    return render(request, 'wordlists/index.html', context)


def wordlist(request, id):
    current_list = get_object_or_404(Wordlist, pk=id)
    current_list.id = id
    test_form = TestForm()
    test_form.fields['wordlist'].initial = current_list.id
    context = {'wordlist': current_list, 'test_form': test_form}
    return render(request, 'wordlists/wordlist.html', context)


def test(request, id, success):
    test = get_object_or_404(Test, pk=id)
    if (success):
        test.correct_count += 1
    if (test.finished()):
        test.completed = True
        successful = test.correct_count
        all = test.word_count
        ratio = float(successful) / float(all)
        reaction = "Logotastisch!" if ratio > 0.8 else "Genial!" if ratio > 0.5 else "Super!"
        context = {"count": successful, "count_all": all, 'reaction': reaction}
        return render(request, 'wordlists/auswertung.html', context)
    context = {'word': test.next_word(), 'id': test.pk,
               'duration': test.duration}
    return render(request, 'wordlists/display_word.html', context)


def start_test(request):
    if request.method == 'GET':
        form = TestForm(request.GET)
        if form.is_valid():
            wordlist = get_object_or_404(Wordlist, pk=form['wordlist'].value())
            new_test = init_test(
                wordlist, form['teilnehmer'].value(), form['duration'].value())
            print(new_test)
            new_test.save()
            context = {'word': new_test.next_word(), 'id': new_test.pk,
                       'duration': new_test.duration}
            return render(request, 'wordlists/display_word.html', context)
        print(request)
    else:
        form = TestForm()
    return render(request, 'wordlists/wordlist.html', {start_test: form})


def init_test(wordlist, participant, duration):
    new_test = Test()
    new_test.wordlist = wordlist
    new_test.participant = participant
    new_test.duration = duration
    words = wordlist.words.splitlines()
    shuffle(words)
    new_test.shuffled_words = "\n".join(words)
    return new_test

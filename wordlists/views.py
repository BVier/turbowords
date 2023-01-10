from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
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
    context = {'wordlist': current_list}
    return render(request, 'wordlists/wordlist.html', context)


def start_test(request, wordlist, participant):
    new_test = Test()
    new_test.wordlist = get_object_or_404(Wordlist, pk=wordlist)
    new_test.participant = participant
    new_test.duration = new_test.wordlist.duration
    words = new_test.wordlist.words.splitlines()
    shuffle(words)
    new_test.shuffled_words = "\n".join(words)
    new_test.word_count = 0
    new_test.correct_count = 0
    new_test.completed = False
    new_test.save()
    context = {'word': new_test.next_word(), 'id': new_test.pk,
               'duration': new_test.duration}
    return render(request, 'wordlists/display_word.html', context)


def test(request, id, success):
    test = get_object_or_404(Test, pk=id)
    if(success):
        test.correct_count += 1
    if(test.finished()):
        test.completed = True
        context = {"count": test.correct_count, "count_all": test.word_count}
        return render(request, 'wordlists/auswertung.html', context)
    context = {'word': test.next_word(), 'id': test.pk,
               'duration': test.duration}
    return render(request, 'wordlists/display_word.html', context)

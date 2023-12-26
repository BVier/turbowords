from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from random import shuffle

# Create your views here.


def startpage(request):
    login_form = LoginForm()
    return render(request, 'wordlists/login.html', {'login_form': login_form})


def login_user(request):
    print(request)
    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return index(request)
    return startpage(request)


@login_required
def index(request):
    wordlist_list = Wordlist.objects.filter(
        filter__user=request.user).order_by('-name')[:5]
    for wordlist in wordlist_list:
        wordlist.count_words = len(wordlist.words.splitlines())
    context = {'latest_wordlist_list': wordlist_list}
    return render(request, 'wordlists/index.html', context)


@login_required
def wordlist(request, id):
    current_list = get_object_or_404(Wordlist, pk=id)
    current_list.id = id
    test_form = TestForm()
    test_form.fields['wordlist'].initial = current_list.id
    context = {'wordlist': current_list, 'test_form': test_form}
    return render(request, 'wordlists/wordlist.html', context)


@login_required
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


@login_required
def start_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            wordlist = get_object_or_404(Wordlist, pk=form['wordlist'].value())
            new_test = init_test(
                wordlist, form['duration'].value())
            print(new_test)
            new_test.save()
            context = {'word': new_test.next_word(), 'id': new_test.pk,
                       'duration': new_test.duration}
            return render(request, 'wordlists/display_word.html', context)
        print(request)
    else:
        form = TestForm()
    return render(request, 'wordlists/wordlist.html', {start_test: form})


def init_test(wordlist, duration):
    new_test = Test()
    new_test.wordlist = wordlist
    new_test.duration = duration
    words = wordlist.words.splitlines()
    shuffle(words)
    new_test.shuffled_words = "\n".join(words)
    return new_test


@login_required
def create_wordlist(request):
    editor_form = WordlistForm()
    return render(request, 'wordlists/wordlist_editor.html', {'editor_form': editor_form, 'wordlist.id': 0})


def edit_wordlist(request, id):
    wordlist = get_object_or_404(Wordlist, pk=id)
    editor_form = WordlistForm(instance=wordlist)
    return render(request, 'wordlists/wordlist_editor.html', {'editor_form': editor_form, 'wordlist': wordlist})

def save_new_list(request):
    form = WordlistForm(request.POST)
    if not form or not form.is_valid:
        return render(request, 'wordlists/wordlist_editor.html', {'editor_form': form, 'wordlist.id': id})
    wordlist = form.save()
    mapping = UserWordlists()
    mapping.wordlist = wordlist
    mapping.user = request.user
    mapping.save()
    return index(request)


def save_list(request, id):
    form = WordlistForm(request.POST)
    if not form or not form.is_valid:
        return render(request, 'wordlists/wordlist_editor.html', {'editor_form': form, 'wordlist.id': id})
    existingList = Wordlist(pk=id)
    form = WordlistForm(request.POST, instance=existingList)
    form.save()
    return index(request)

def delete_wordlist(request, id):
    wordlist = get_object_or_404(Wordlist, pk=id)
    mapping = get_object_or_404(
        UserWordlists, user=request.user, wordlist=wordlist)
    mapping.delete()
    if UserWordlists.objects.filter(wordlist=wordlist).count():
        wordlist.delete()
    return index(request)

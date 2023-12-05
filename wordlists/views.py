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
            return patients(request)
    return startpage(request)


@login_required
def index(request):
    currentPatient = get_patient_from_cookie(request)
    if not currentPatient:
        return patients()
    wordlist_list = Wordlist.objects.filter(
        filter__user=request.user).order_by('-name')
    for wordlist in wordlist_list:
        wordlist.count_words = len(wordlist.words.splitlines())
    context = {'latest_wordlist_list': wordlist_list,
               'patient': currentPatient}
    return render(request, 'wordlists/index.html', context)


@login_required
def wordlist(request, id):
    wordlist = get_object_or_404(Wordlist, pk=id)
    # test_form = TestForm()
    # context = {'wordlist': current_list, 'test_form': test_form}
    # response = render(request, 'wordlists/wordlist.html', context)
    # response = start_test(request)
    patient = get_patient_from_cookie(request)
    if not patient:
        return patients()  # TODO: with error message
    # wordlist = get_wordlist_from_cookie(request)
    if not wordlist:
        return index()  # TODO: with error message
    new_test = init_test(wordlist, patient, patient.duration)
    context = {'word': new_test.next_word(), 'id': new_test.pk,
               'duration': new_test.duration}
    response = render(request, 'wordlists/display_word.html', context)
    response.set_cookie('wordlist', id)
    return start_test(response)


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
    # if request.method == 'POST':
    #     form = TestForm(request.POST)
    #     if form.is_valid():
    patient = get_patient_from_cookie(request)
    if not patient:
        return patients()  # TODO: with error message
    wordlist = get_wordlist_from_cookie(request)
    if not wordlist:
        return patients()  # TODO: with error message
    new_test = init_test(
        wordlist, patient, patient.duration)
    context = {'word': new_test.next_word(), 'id': new_test.pk,
               'duration': new_test.duration}
    return render(request, 'wordlists/display_word.html', context)
    # else:
    #     form = TestForm()
    # return render(request, 'wordlists/wordlist.html', {start_test: form})


def init_test(wordlist, patient, duration):
    new_test = Test()
    new_test.wordlist = wordlist
    new_test.patient = patient
    new_test.duration = duration
    words = wordlist.words.splitlines()
    shuffle(words)
    new_test.shuffled_words = "\n".join(words)
    new_test.save()
    return new_test


@login_required
def create_wordlist(request):
    editor_form = WordlistForm()
    return render(request, 'wordlists/wordlist_editor.html', {'editor_form': editor_form, 'wordlist.id': 0})


@login_required
def edit_wordlist(request):
    wordlist = get_wordlist_from_cookie(request)
    editor_form = WordlistForm(instance=wordlist)
    return render(request, 'wordlists/wordlist_editor.html', {'editor_form': editor_form, 'wordlist': wordlist})


@login_required
def add_wordlist(request):
    form = WordlistForm(request.POST)
    if not form or not form.is_valid:
        return render(request, 'wordlists/wordlist_editor.html', {'editor_form': form, 'wordlist.id': id})
    wordlist = form.save()
    mapping = UserWordlists()
    mapping.wordlist = wordlist
    mapping.user = request.user
    mapping.save()
    return index(request)


@login_required
def save_list(request, id):
    form = WordlistForm(request.POST)
    if not form or not form.is_valid:
        return render(request, 'wordlists/wordlist_editor.html', {'editor_form': form, 'wordlist.id': id})
    existingList = Wordlist(pk=id)
    form = WordlistForm(request.POST, instance=existingList)
    form.save()
    return index(request)


@login_required
def delete_wordlist(request):
    wordlist = get_wordlist_from_cookie(request)
    mapping = get_object_or_404(
        UserWordlists, user=request.user, wordlist=wordlist)
    mapping.delete()
    if UserWordlists.objects.filter(wordlist=wordlist).count():
        wordlist.delete()
    return index(request)


@login_required
def patients(request):
    patient_list = Patient.objects.filter(
        therapist=request.user).order_by('-Vorname')
    patient_form = PatientForm()
    context = {'patient_list': patient_list, 'patient_form': patient_form}
    return render(request, 'wordlists/patients.html', context)


@login_required
def add_patient(request):
    form = PatientForm(request.POST)
    patient = form.save(commit=False)
    patient.therapist = request.user
    if Patient.objects.filter(therapist=patient.therapist, Vorname=patient.Vorname, Nachname=patient.Nachname).count() > 0:
        return patients(request)
    patient.save()
    return patients(request)


@login_required
def set_patient(request, patientId):
    currentPatient = get_object_or_404(Patient, pk=patientId)
    if not currentPatient:
        return patients()
    wordlist_list = Wordlist.objects.filter(
        filter__user=request.user).order_by('-name')
    for wordlist in wordlist_list:
        wordlist.count_words = len(wordlist.words.splitlines())
    context = {'latest_wordlist_list': wordlist_list,
               'patient': currentPatient}
    response = render(request, 'wordlists/index.html', context)

    response.set_cookie('patientId', patientId)
    return response


"""
Helper methods
"""


def get_wordlist_from_cookie(request):
    wordlistId = request.COOKIES.get('wordlist')
    return Wordlist.objects.filter(pk=wordlistId).first()


def get_patient_from_cookie(request):
    patientId = request.COOKIES.get('patientId')
    return Patient.objects.filter(pk=patientId).first()

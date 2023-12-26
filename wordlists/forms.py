from django import forms
from wordlists.models import Wordlist

class TestForm(forms.Form):
    """Form to init test"""
    wordlist = forms.IntegerField(
        label='Wordlist', required=True, widget=forms.HiddenInput)
    duration = forms.IntegerField(
        label='Anzeigedauer (ms)', min_value=10, initial=1000, required=True)


class LoginForm(forms.Form):
    """Login form"""
    username = forms.CharField(label='Username', required=True, max_length=60)
    password = forms.CharField(
        widget=forms.PasswordInput, label='Password', required=True)


class EditorForm(forms.Form):
    """Form for Wordlist editor"""
    name = forms.CharField(label='Name der Liste', max_length=100)
    words = forms.CharField(
        label='Wörter (ein Wort pro Zeile)', widget=forms.Textarea)

class WordlistForm(forms.ModelForm):
    class Meta:
        model = Wordlist
        fields = ['name', 'words']
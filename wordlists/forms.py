from django import forms
from wordlists.models import Wordlist, Patient

class TestForm(forms.Form):
    """Form to init test"""
    duration = forms.IntegerField(
        label='Anzeigedauer (ms)', min_value=10, initial=1000, required=True)


class LoginForm(forms.Form):
    """Login form"""
    username = forms.CharField(label='Username', required=True, max_length=60)
    password = forms.CharField(
        widget=forms.PasswordInput, label='Password', required=True)

class WordlistForm(forms.ModelForm):
    class Meta:
        model = Wordlist
        fields = ['name', 'words']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['Vorname', 'Nachname', 'Anzeige (in ms)']
from django import forms

class TestForm(forms.Form):
    """Form to init test"""
    wordlist = forms.IntegerField(label='Wordlist', required=True, widget=forms.HiddenInput)
    teilnehmer = forms.CharField(label='Teilnehmer', max_length=100, required=True)
    duration = forms.IntegerField(label='Anzeigedauer (ms)', min_value=10, initial=1000, required=True)

class LoginForm(forms.Form):
    """Login form"""
    username = forms.CharField(label='Username', required=True, max_length=60)
    password = forms.CharField(widget = forms.PasswordInput,label='Password', required=True)
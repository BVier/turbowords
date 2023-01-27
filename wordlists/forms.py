from django import forms

class TestForm(forms.Form):
    """Form to init test"""
    wordlist = forms.IntegerField(label='Wordlist', required=True, widget=forms.HiddenInput)
    teilnehmer = forms.CharField(label='Teilnehmer', max_length=100, required=True)
    duration = forms.IntegerField(label='Anzeigedauer (ms)', min_value=10, initial=1000, required=True)

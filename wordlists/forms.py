from django import forms

class TestForm(forms.Form):
    # TODO b4
    your_name = forms.CharField(label='Your name', max_length=100)
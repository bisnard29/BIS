from django import forms

class SpesoForm(forms.Form):
    mailto = forms.EmailField()
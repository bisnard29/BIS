from django import forms

class SpesoForm(forms.Form):
    mailto = forms.EmailField()
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
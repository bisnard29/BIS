from django import forms

class SpesoForm(forms.Form):
    mailto = forms.EmailField(label='Your email address')
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
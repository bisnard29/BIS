from django import forms

class PayForm(forms.Form):
    mailto = forms.EmailField(label='Your email address')
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
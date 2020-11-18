from django import forms

class ContactusForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    subject=forms.CharField(max_length=300)
    message=forms.CharField(widget=forms.Textarea)


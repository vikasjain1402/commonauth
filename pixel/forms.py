from django.forms import ModelForm,Textarea
from django import forms
from .models import Task

class ImageUploadFormOld(forms.Form):
    imageUpload=forms.ImageField(label="Upload Image",
            widget=forms.FileInput(attrs={'class':'form-control'}))
    requiredSize=forms.IntegerField(label="filesize Required",
            initial=200000,widget=forms.NumberInput(attrs={'class':'form-control'}))


class ImageUploadForm(ModelForm):
    #ImageUpload=image(max_length=200)
    #requiredSize=requiredSize()
    class Meta:
        model=Task
        exclude=['user']
        #fields='__all__'


from django import forms


class ImageUploadForm(forms.Form):
    imageUpload=forms.ImageField(label="Upload Image",widget=forms.FileInput())
    requiredSize=forms.IntegerField(label="filesize Required")

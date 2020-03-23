from django import forms

#pour télécharger fichiers
class UploadDocumentForm(forms.Form):
    file = forms.FileField()
    image = forms.ImageField()

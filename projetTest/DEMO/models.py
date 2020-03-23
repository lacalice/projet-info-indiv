from django.db import models



class Essai(models.Model):
    titre = models.CharField(max_length=30)
    auteur = models.CharField(max_length=30)
    contenu = models.CharField(max_length=1000, default='SOME STRING')

    def __str__(self):
        return self.titre

    

#class Document(models.Model):
#    docfile = models.FileField(upload_to='fichier')


#class DocumentForm(forms.Form):
#    docfile = forms.FileField(label='Selectionner un fichier',
#                          help_text='Taille max.: 42 megabytes')

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django import forms
from django.views.generic import ListView
from .models import Essai
from django.template import RequestContext
from .forms import UploadDocumentForm
from django.views.generic import TemplateView

# Create your views here.
def home(request) :
    return render(request,'DEMO/index.html')

def home02(request):
    return render (request,'DEMO/home-02.html')

def contact(request):
    return render (request,'DEMO/contact.html')

def category02(request):
    return render (request,'DEMO/category-02.html')

def category01(request):
    return render (request,'DEMO/category-01.html')

def bloglist02(request):
    return render (request,'DEMO/blog-list-02.html')

def bloglist01(request):
    return render (request,'DEMO/blog-list-01.html')

def bloggrid(request):
    return render (request,'DEMO/blog-grid.html')

def blogdetail2(request):
    return render (request,'DEMO/blog-detail-02.html')

def blogdetail1(request):
    return render (request,'DEMO/blog-detail-01.html')

def about(request):
    return render (request,'DEMO/about.html')

def numeros(request):
    return render (request,'DEMO/numeros.html')

class EssaiListView(ListView):
    model = Essai
    template_name = 'DEMO/login.html'
    context_object_name = 'test'

#def essai_view(ListView):
#    test = Essai.objects.all()
#    return render(ListView, 'DEMO/login.html', {'test':test})



#fonction pour la connexion de l'admin
def login_request(request):
    if request.method == 'POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            if user is not None :
                login(request,user)
                messages.info(request,f"vous êtes connecté ! youpi !")
                return redirect("index.html")
            else :
                messages.error(request,f"Mauvais mdp ou nom")
             
        else:
            messages.error(request,f"problemes lors de la connexion")
    form = AuthenticationForm()
    return render(request=request,template_name='DEMO/login.html',context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("DEMO/index.html")

#télécharger fichier comme PDF
#def upload_doc(request):
#    form = UploadDocumentForm()
#    if request.method == 'POST':
#        form = UploadDocumentForm(request.POST, request.FILES)
#        if form.is_valid():
#             form.save()
#    return render(request, 'numeros', locals())

##def AddDoc(request):
#    if request.method == 'POST':
#        form = DocumentForm(request.POST, request.FILES)
#        if form.is_valid():
#            newdoc = Document(docfile = request.FILES['docfile'])
#            newdoc.save()
#            return HttpResponseRedirect('')
#    else:
#        form = DocumentForm()

#    documents = Document.objects.all()

#    return render('numeros.html',
#                             {'documents': documents,'form': form},
#                               context=RequestContext(request)
#                              )

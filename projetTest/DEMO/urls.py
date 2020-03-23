from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import EssaiListView

urlpatterns = [
    path('index.html', views.home, name='page accueil'),
    path('home-02.html', views.home02, name='page'),
    path('contact.html', views.contact, name='contact'),
    path('category-02.html', views.category02, name='category02'),
    path('category-01.html', views.category01, name='category01'),
    path('blog-list-02.html', views.bloglist02, name='bloglist02'),
    path('blog-list-01.html', views.bloglist01, name='bloglist01'),
    path('blog-grid.html', views.bloggrid, name='bloggrid'),
    path('blog-detail-02.html', views.blogdetail2, name='blogdetail2'),
    path('blog-detail-01.html', views.blogdetail1, name='blogdetail1'),
    path('about.html', views.about, name='about'),
    path("login.html/", views.login_request, name="login"),
    path('index.html', views.logout_request, name="logout"),
    path('numeros.html', views.numeros, name="numeros"),
    path('essai_view/', EssaiListView.as_view(), name='essai_view/'),
]

urlpatterns += staticfiles_urlpatterns()
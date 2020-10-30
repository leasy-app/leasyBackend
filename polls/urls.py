from django.urls import path

from . import views

urlpatterns = [

    path('Categories/', views.getCategories, name='index'),
    path('Posts/', views.getPosts, name='index'),
    path('Likes/', views.getLikes, name='index'),
    path('Reads/', views.getReads, name='index'),
    path('Marks/', views.getMarks, name='index'),
    path('AddCategorie/', views.AddCategorie, name='index'),
    path('AddPost/', views.AddPost, name='index'),
]
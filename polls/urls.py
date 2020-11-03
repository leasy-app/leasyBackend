from django.urls import path , re_path

from . import views

urlpatterns = [

    path('Categories/', views.getCategories, name='index'),
    path('Posts/', views.getPosts, name='index'),
    path('Likes/', views.getLikes, name='index'),
    path('Reads/', views.getReads, name='index'),
    path('Marks/', views.getMarks, name='index'),
    path('AddCategorie/', views.AddCategorie, name='index'),
    path('AddPost/', views.AddPost, name='index'),
    path('AddLike/', views.AddLike, name='index'),
    path('AddRead/', views.AddRead, name='index'),
    path('AddMark/', views.AddMark, name='index'),
    path('AddFullPost/', views.AddFullPost, name='index'),
    path('Content/', views.getContent, name='index'),
    path('upload', views.FileUploadView, name='index'),
    path('download', views.download, name='index'),

]
from django.contrib.gis.geometry import json_regex
from django.shortcuts import render
from django.http import JsonResponse , HttpRequest , HttpResponse
import json

from pip._vendor.requests import request

from .models import *
from datetime import datetime

def getCategories(request):
    return JsonResponse(list(Categories.objects.all().values()) , safe=False)

def getPosts(request):
    categorie = request.GET.get('categorie')
    writer = request.GET.get('writer')
    if categorie and writer:
        categorie = Categories.objects.filter(Name=categorie)
        writer = User.objects.filter(Id=writer)
        if len(categorie) == 0 or len(writer) == 0:
            return JsonResponse({"valu": False})
        return JsonResponse(list(Post.objects.filter(categorie=categorie[0] , Writer=writer[0]).values()), safe=False)
    elif categorie:
        categorie = Categories.objects.filter(Name=categorie)
        if len(categorie) == 0 :
            return JsonResponse({"valu": False})
        return JsonResponse(list(Post.objects.filter(categorie=categorie[0]).values()), safe=False)
    elif writer:
        writer = User.objects.filter(Id=writer)
        if len(writer) == 0:
            return JsonResponse({"valu": False})
        return JsonResponse(list(Post.objects.filter(Writer=writer[0]).values()), safe=False)
    return JsonResponse(list(Post.objects.all().values()), safe=False)

def getLikes(request):
    user_id = request.GET.get('user')
    post_id = request.GET.get('post')
    if user_id:
        user = User.objects.filter(Id=user_id)
        if len(user) ==0:
            return JsonResponse({"valu" : False})
        return JsonResponse(list(Likes.objects.filter(user=user[0]).values()) , safe=False)
    elif post_id:
        ##TODO post int nabashe
        post = Post.objects.filter(Id=int(post_id))
        if len(post) == 0:
            return JsonResponse({"valu": False})
        return JsonResponse(list(Likes.objects.filter(post=post[0]).values()), safe=False)
    else:
        return JsonResponse(list(Likes.objects.all().values()), safe=False)

def getReads(request):
    user_id = request.GET.get('user')
    post_id = request.GET.get('post')
    if user_id:
        user = User.objects.filter(Id=user_id)
        if len(user) ==0:
            return JsonResponse({"valu" : False})
        return JsonResponse(list(ReadsPost.objects.filter(user=user[0]).values()) , safe=False)
    elif post_id:
        ##TODO post int nabashe
        post = Post.objects.filter(Id=int(post_id))
        if len(post) == 0:
            return JsonResponse({"valu": False})
        return JsonResponse(list(ReadsPost.objects.filter(post=post[0]).values()), safe=False)
    else:
        return JsonResponse(list(ReadsPost.objects.all().values()), safe=False)


def getMarks(request):
    user_id = request.GET.get('user')
    post_id = request.GET.get('post')
    if user_id:
        user = User.objects.filter(Id=user_id)
        if len(user) ==0:
            return JsonResponse({"valu" : False})
        return JsonResponse(list(Mark.objects.filter(user=user[0]).values()) , safe=False)
    elif post_id:
        ##TODO post int nabashe
        post = Post.objects.filter(Id=int(post_id))
        if len(post) == 0:
            return JsonResponse({"valu": False})
        return JsonResponse(list(Mark.objects.filter(post=post[0]).values()), safe=False)
    else:
        return JsonResponse(list(Mark.objects.all().values()), safe=False)


def AddCategorie(request):
    name = request.GET.get('name')
    photo = request.GET.get('photo')
    if not(name and photo):
        return JsonResponse({"valu": False})
    categorie = Categories.objects.create(Name=name, Photo=photo)
    return JsonResponse({"valu": True})

def AddPost(request):
    name = request.GET.get('name')
    photo = request.GET.get('photo')
    categorie_name = request.GET.get('categorie')
    writer_id = request.GET.get('writer')
    if not(name and photo and categorie_name and writer_id):
        return JsonResponse({"valu": False})
    categorie = Categories.objects.filter(Name=categorie_name)
    if len(categorie) == 0:
        return JsonResponse({"valu": False})
    writer = User.objects.filter(Id=writer_id)
    post = Post.objects.create(Name=name, categorie=categorie[0], Header_photo=photo, Writer=writer[0])
    return JsonResponse({"valu": True})





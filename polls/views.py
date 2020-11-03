from django.contrib.gis.geometry import json_regex
from django.shortcuts import render
from django.http import JsonResponse , HttpRequest , HttpResponse
import json

from pip._vendor.requests import request
from django.http import HttpResponse, Http404, StreamingHttpResponse, FileResponse
from .models import *
from datetime import datetime
import os
from .models import Content


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
    summary = request.GET.get('summary')
    if not(name and photo and categorie_name and writer_id , summary):
        return JsonResponse({"valu": False})
    categorie = Categories.objects.filter(Name=categorie_name)
    if len(categorie) == 0:
        return JsonResponse({"valu": False})
    writer = User.objects.filter(Id=writer_id)
    if len(writer) == 0:
        return JsonResponse({"valu": False})
    post = Post.objects.create(Name=name, categorie=categorie[0], Header_photo=photo, Writer=writer[0] , Summary = summary)
    return JsonResponse({"valu": True})

def AddFullPost(request):
    name = request.GET.get('name')
    photo = request.GET.get('photo')
    categorie_name = request.GET.get('categorie')
    writer_id = request.GET.get('writer')
    content1 = request.GET.get('content1')
    content2 = request.GET.get('content2')
    main_content = request.GET.get('main_content')
    summary = request.GET.get('summary')
    if not (name and photo and categorie_name and writer_id and content1 and content2 and main_content and summary):
        return JsonResponse({"valu": False})

    categorie = Categories.objects.filter(Name=categorie_name)
    if len(categorie) == 0:
        return JsonResponse({"valu": False})

    writer = User.objects.filter(Id=writer_id)
    if len(writer) == 0:
        return JsonResponse({"valu": False})

    post = Post.objects.create(Name=name, categorie=categorie[0], Header_photo=photo, Writer=writer[0] , Summary = summary)

    content = Post.objects.create(Id=post, Content1=content1, Content2=content2, Main_content=main_content)
    return JsonResponse({"valu": True})

def AddMark(request):
    user_id = request.GET.get('user')
    post_id = request.GET.get('post')
    if not(user_id and post_id):
        return JsonResponse({"valu": False})
    user = User.objects.filter(Id=user_id)
    if len(user) ==0:
        return JsonResponse({"valu" : False})

    ##TODO post int nabashe
    post = Post.objects.filter(Id=int(post_id))
    if len(post) == 0:
        return JsonResponse({"valu": False})
    mark = Mark.objects.create(user = user[0] , post = post[0])
    return JsonResponse({"valu": True})

def AddLike(request):
    user_id = request.GET.get('user')
    post_id = request.GET.get('post')
    if not(user_id and post_id):
        return JsonResponse({"valu": False})
    user = User.objects.filter(Id=user_id)
    if len(user) == 0:
        return JsonResponse({"valu": False})

    ##TODO post int nabashe
    post = Post.objects.filter(Id=int(post_id))
    if len(post) == 0:
        return JsonResponse({"valu": False})
    like = Likes.objects.create(user=user[0], post=post[0])
    return JsonResponse({"valu": True})

def AddRead(request):
    user_id = request.GET.get('user')
    post_id = request.GET.get('post')
    if not(user_id and post_id):
        return JsonResponse({"valu": False})


    user = User.objects.filter(Id=user_id)
    if len(user) == 0:
        return JsonResponse({"valu": False})

    ##TODO post int nabashe
    post = Post.objects.filter(Id=int(post_id))
    if len(post) == 0:
        return JsonResponse({"valu": False})
    reads = ReadsPost.objects.create(user=user[0], post=post[0])
    return JsonResponse({"valu": True})

def getContent(request):
    categorie = request.GET.get('categorie')
    writer = request.GET.get('writer')
    id = request.GET.get('id')
    post = 0
    if id:
    ##TODO post int nabashe
        post = Post.objects.filter(Id=int(id)).values()
    elif categorie and writer:
        categorie = Categories.objects.filter(Name=categorie)
        writer = User.objects.filter(Id=writer)
        if len(categorie) == 0 or len(writer) == 0:
            return JsonResponse({"valu": False})
        post = Post.objects.filter(categorie=categorie[0], Writer=writer[0]).values()
    elif categorie:
        categorie = Categories.objects.filter(Name=categorie)
        if len(categorie) == 0:
            return JsonResponse({"valu": False})
        post = Post.objects.filter(categorie=categorie[0]).values()
    elif writer:
        writer = User.objects.filter(Id=writer)
        if len(writer) == 0:
            return JsonResponse({"valu": False})
        post = Post.objects.filter(Writer=writer[0]).values()
    if not (post==0) and len(post) > 0:
        content = []
        for i in post:
            content.append(list(Content.objects.filter(id=i).values()))
        return JsonResponse(content, safe=False)
    else:
        return JsonResponse(list(Content.objects.all().values()), safe=False)




def FileUploadView(request):
    if request.FILES:
        file = File.objects.create(request.FILES)
        return JsonResponse({'name':file.file.name}, safe=False)
    else:
        return JsonResponse({'valu':False},safe=False)

import os
from django.conf import settings
from django.http import HttpResponse, Http404

def download(request):
    path = 'Sunflower-field-Fargo-North-Dakota.jpg'
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404






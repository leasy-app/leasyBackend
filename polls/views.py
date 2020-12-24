from django.contrib.gis.geometry import json_regex
from django.shortcuts import render
from django.http import JsonResponse , HttpRequest , HttpResponse
import json

from pip._vendor.requests import request
from django.http import HttpResponse, Http404, StreamingHttpResponse, FileResponse
from .models import *
from datetime import datetime
import os
import time


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

    content = Content.objects.create(Id=post, Content1=content1, Content2=content2, Main_content=main_content)
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
        #return HttpResponse("HI")
        #return JsonResponse(list(post), safe=False)
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
    if not (post==0):
 #       if len(post) ==0:
  #          return JsonResponse({"valu": False})
        content = []
        for i in post:
            content.append(list(Content.objects.filter(Id=i.get("Id")).values()))
        return JsonResponse(content, safe=False)
    else:
        return JsonResponse(list(Content.objects.all().values()), safe=False)




def FileUploadView(request):
    if request.FILES:
        file = File2.objects.create(request.FILES)
        return JsonResponse({'name':file.file.name}, safe=False)
    else:
        return JsonResponse({'valu':False},safe=False)

def FileUploadView0(request):
    if request.FILES:
        file = File2.objects.create(request.FILES)
        file.file.name = request.FILES
        file.save()
        return JsonResponse({'name':file.file.name}, safe=False)
    else:
        return JsonResponse({'valu':False},safe=False)

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import MyFileSerializer


class upload(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = MyFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




import os
from django.conf import settings
from django.http import HttpResponse, Http404
import mimetypes

def download(request):
    path = request.GET.get('name')
    file_path = os.path.join(settings.MEDIA_ROOT, path)

    #return  JsonResponse(list(File2.objects.filter(file=path).values()),safe=False)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), mimetypes.guess_type(path)[0])
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
def AddCourse(request):
#?name=none&picture=NoPic&explanation=simpleCourse&posts=1-19
    #return HttpResponse("hi")
    name = request.GET.get('name')
    picture = request.GET.get('picture')
    explanation = request.GET.get('explanation')
    post = request.GET.get('posts')

    if not(name and picture and explanation and post):
        return JsonResponse({"valu": False})
    course = Course.objects.create(Name=name , Picture=picture , Explanation=explanation)
    plist = []
    for i in post.split('-'):
        p = Post.objects.filter(Id=int(i))
        if len(p) ==0:
            return JsonResponse({"valu": False})
        plist.append(p)
    for i in plist:
        uCourse_Post.objects.create(course=course,post=i[0])
    return JsonResponse({"valu": True})

def AddPost2Course(request):
    course = request.GET.get('course')
    post = request.GET.get('post')

    if not (course and post):
        return JsonResponse({"valu": False})

    p = Post.objects.filter(Id=int(post))
    if len(p) == 0:
        return JsonResponse({"valu": False})

    c = Course.objects.filter(Id=int(course))
    if len(c) == 0:
        return JsonResponse({"valu": False})

    uCourse_Post.objects.create(course=c[0],post=p[0])
    return JsonResponse({"valu": True})


def GetCourse(request):
    course = request.GET.get('course')
    if not (course):
        return JsonResponse(list(Course.objects.values()),safe=False)
    return JsonResponse(list(Course.objects.filter(Id=int(course)).values()),safe=False)


def GetCoursePost(request):
    course = request.GET.get('course')
    if not (course):
        return JsonResponse({"valu": False})
    list = []
    for i in uCourse_Post.objects.filter(course=int(course)).values():
        m = i.get('post_id')
        list.append((Post.objects.filter(Id=i.get('post_id')).values()[0]))
    return JsonResponse(list,safe=False)






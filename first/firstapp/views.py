from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import *
# Create your views here.


def index(request):
    # return HttpResponse('<h1>hello world</h1>')
    # context = {'title': 'Django首页', 'list': range(1, 10)}
    # return render(request, 'firstapp/index.html', context)
    booklist = BookInfo.objects.all()
    context = {'title': '图书首页', 'booklist': booklist}
    return render(request, 'firstapp/index2.html', context)


def book(request, id):
    herolist = BookInfo.objects.get(id=id).heroinfo_set.all()
    context = {'title': '人物首页', 'herolist': herolist}
    return render(request, 'firstapp/index3.html', context)

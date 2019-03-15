from django.shortcuts import render,HttpResponse

# Create your views here.

def userinfo(request):
    return HttpResponse(b'Hello')

def index(request):
    return HttpResponse(b'<h1>wellcome here</h1>')
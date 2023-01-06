from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get(request):
 return render (request, "info/index-get.html") 

def post(request):
 return render(request, "info/index-post.html")

def printget(request):
  return render(request, "info/print-get.html")

def printpost(request):
  return render(request, "info/print-post.html")
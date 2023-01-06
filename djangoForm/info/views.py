from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get(request):
 return render (request, "info/index-get.html") 

def post(request):
 return render(request, "info/index-post.html")
from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class InfoForm(forms.Form):
  form = forms.CharField(label="Email")

def get(request):
 return render (request, "info/index-get.html", {
  "form" : InfoForm
 }) 

def post(request):
 return render(request, "info/index-post.html")

def printget(request):
  return render(request, "info/print-get.html")

def printpost(request):
  return render(request, "info/print-post.html")
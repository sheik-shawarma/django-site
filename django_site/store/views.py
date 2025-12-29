from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Yooo sup world. <br>Esse é o views index")
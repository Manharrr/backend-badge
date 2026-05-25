from django.shortcuts import render
# from rest_framework .views import APIView
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello")
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getPosts(request):
    return HttpResponse("Here are the posts!")
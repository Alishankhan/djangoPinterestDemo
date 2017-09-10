from django.shortcuts import render
from django.http import HttpResponse
from backend.models import Post
# Create your views here.

def index(request):

    posts = Post.object.order_by('dateCreated')[:10]

    return HttpResponse("Test!!!")

def detail(request, slug):
    # post = Post.objects.
    return HttpResponse(slug)
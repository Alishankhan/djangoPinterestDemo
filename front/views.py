from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from backend.models import Post
# Create your views here.

def index(request):

    # posts = Post.objects.order_by('dateCreated')[:10]
    template = loader.get_template('front/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def detail(request, slug):

    # post = Post.objects.
    return HttpResponse(slug)
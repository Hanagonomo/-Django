
from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Post
from datetime import datetime

def homepage(request):
	posts = Post.objects.all()
	now = datetime.now()
	return render(request, 'index.html', locals())

def	showpost(request, slug):
	try:
		post = Post.objects.get(slug = slug)
		if post != None:
			return render(request, 'post.html', locals())
	except:
		return redirect('/')

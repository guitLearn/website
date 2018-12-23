# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.'
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime
from .models import Post

def homepage(request):
	template = get_template('index.html')
	posts = Post.objects.all()
	now = datetime.now()
	html = template.render(locals())
	return HttpResponse(html)

def showpost(request, slug):
	template = get_template('post.html')
	now = datetime.now()
	try:
		post = Post.objects.get(slug=slug)
		if post != None:
			html = template.render(locals())
			return HttpResponse(html)
		else:
			return redirect('/')			
	except:
		return redirect('/')

from typing import KeysView
from django import db, forms
from django.core.files.base import ContentFile
from django.db import models
from django.http import request
from django.urls.base import reverse_lazy
from django.views.generic.base import ContextMixin
from django.views.generic.edit import DeleteView
from blog.forms import PostForm
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Post
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse

class post_list(ListView):
    model = Post
    queryset = Post.objects.order_by('-id')

class post_detail(DetailView):
    model = Post

class post_new(CreateView):
    template_name = 'blog/post_edit.html'
    model = Post
    form_class = PostForm
    success_url = '/'


class post_edit(UpdateView):
    template_name = 'blog/post_edit.html'
    model = Post
    form_class = PostForm
    success_url = '/'

class post_delete(DeleteView):
    template_name ='blog/post_delete.html'
    model = Post
    success_url = '/'



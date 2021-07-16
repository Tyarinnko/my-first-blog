import blog
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
from django.views.generic import ListView,DetailView,CreateView,UpdateView

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

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        form.instance.published_date = timezone.now()
        return super(post_new,self).form_valid(form)

class post_edit(UpdateView):
    template_name = 'blog/post_edit.html'
    model = Post
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        form.instance.published_date = timezone.now()
        return super(post_edit,self).form_valid(form)

class post_delete(DeleteView):
    template_name = 'blog/post_delete.html'
    model = Post
    form_class = PostForm
    success_url = '/'
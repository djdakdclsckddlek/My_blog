from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class PostListView(ListView):

    model = Post
    template_name = 'blog/post_list.html'


class PostDetailView(DetailView):

    template_name = 'blog/post_detail.html'
    queryset = Post.objects.all()

    def get_object(self, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return post


class PostCreateView(LoginRequiredMixin, CreateView):

    template_name = 'blog/post_create.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_detail')

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'blog/post_update.html'
    model = Post
    fields = ['title', 'content']

    def get_object(self, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        if post.author != self.request.user:
            raise HttpResponse('글을 수정할 수 있는 권한이 없습니다!')
        return post

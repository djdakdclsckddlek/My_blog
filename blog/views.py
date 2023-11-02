from typing import Any
from accounts.models import User
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.core.exceptions import PermissionDenied
from django.views import View

from django.conf import settings
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
import os
from uuid import uuid4


class PostListView(ListView):

    model = Post
    template_name = 'blog/post_list.html'
    
    #게시물 검색
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(content__icontains=q) | Q(author__nickname__icontains=q))
        return qs
    


class PostListUserView(ListView):

    model = Post
    template_name = 'blog/my_post.html'

    # 'user' context에 User저장
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(username=self.kwargs['blog'])
        return context

    # 이름으로 Post목록을 필터링
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        username = self.kwargs['blog']
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(content__icontains=q) | Q(author__nickname__icontains=q))
        return qs.filter(author__username=username).order_by('-created_at')

class PostDeleteView(LoginRequiredMixin, View):
    
    def get(self, request, pk):
        
        post = Post.objects.get(pk=pk)
        #글을 쓴 유저거나 관리자만 글을 지울 수 있음.
        if post.author != request.user and not request.user.is_superuser:
            return redirect('blog:post_detail', pk)
        post.delete()
        
        return redirect('blog:post_list')
    

#인기순으로 글을 정렬
class PostPopularView(ListView):

    model = Post
    template_name = 'blog/post_list.html'
    queryset = Post.objects.all().order_by('-views')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = {'popular': '인기글'}
        return context


class PostDetailView(DetailView):

    template_name = 'blog/post_detail.html'
    queryset = Post.objects.all()

    def get_object(self, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        post.views += 1
        post.save()
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #Comment 모델에서 post 필드가 현재 포스트와 같은 댓글들을 가져와 comments 변수에 할당
        post = self.get_object()
        #새로고침이 일어날때마다 뷰가 늘어나 조정
        post.views -= 1
        post.save()
        comments = Comment.objects.filter(post=post)

        context['comments'] = comments
        context['comment_form'] = CommentForm()
        return context
    
    #댓글과 대댓글을 달기위해 post요청을 보냄.
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        #새로고침이 일어날때마다 뷰가 늘어나 조정
        # 보낼때 한번, redirect될때 한번
        post.views -= 2
        
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            recomment_id = comment_form.cleaned_data.get('recomment')
            #대댓글이 있으면
            if recomment_id:
                recomment_text = Comment.objects.get(id=recomment_id)
                comment.recomment = recomment_text
            
            comment.author = self.request.user
            comment.save()
            post.update_comments_count()
            post.save()
            return redirect(request.get_full_path())  # Redirect to the same URL
        return super().get(request, *args, **kwargs)
        
class PostCreateView(LoginRequiredMixin, CreateView):

    template_name = 'blog/post_create.html'
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.views -= 1

        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'blog/post_create.html'
    model = Post
    form_class = PostForm

    def get_object(self, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        # 글을 수정할 시 작성한 회원이거나 관리자만 글을 수정할 수 있음.
        if post.author == self.request.user or self.request.user.is_superuser:
            return post
        else:
            raise PermissionDenied('글을 수정할 수 있는 권한이 없습니다!')

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})


def fileUpload(request):
    if request.method == 'POST' or request.method == 'GET':
        # 업로드된 파일을 가져옵니다.
        uploaded_file = request.FILES.get('images')
        uuid = str(uuid4())
        if uploaded_file:
            # 파일 확장자를 추출합니다 (xxx.png)
            file_extension = uploaded_file.name.split('.')[-1]

            # 파일을 저장합니다. (---uuid----.png)
            file_name = os.path.join(
                'media/blog/images/', f'{uuid}.{file_extension}')
            with open(file_name, 'wb') as f:
                for chunk in uploaded_file.chunks():
                    f.write(chunk)
            print(file_name)
            # 파일의 URL을 생성합니다. (---uuid----.png)
            file_url = settings.MEDIA_URL + os.path.join(
                'blog/images/', f'{uuid}.{file_extension}')
            print(file_url)
            return JsonResponse({
                'success': True,
                'url': file_url,
            })
        else:
            return JsonResponse({
                'success': False,
                'error': '이미지를 찾을 수 없습니다.',
            })
    else:
        return JsonResponse({
            'success': False,
            'error': '비정상적인 접근입니다.',
        })

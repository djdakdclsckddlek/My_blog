from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from django.views.generic import View, CreateView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import SignupForm, CustomUserChangeForm

# 함수기반 뷰
# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('가입완료.')
#         else:
#             form = SignupForm()

#     return render(request, 'accounts/register.html', {'form':form})


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    # 회원가입시 입력한 정보로 로그인
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('blog:post_list')


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    next_page = reverse_lazy('blog:post_list')


class UserLogoutView(LogoutView):
    next_page = 'blog:post_list'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user

    # 'profile_user' context에 현재 User저장
    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['profile_user'] = self.request.user
        return context


@login_required
def user_profile(request):
    user = request.user
    # 링크의 이메일을 db에서 찾음 // 없으면 404페이지
    user = get_object_or_404(User, pk=user.pk)

    # 로그인한 이메일과 링크의 이메일이 같은지 확인
    if request.user.email == user.email:
        context = {'profile_user': user}
        return render(request, 'accounts/profile.html', context)

    else:
        return HttpResponse('장난치지마라')

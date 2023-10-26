from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import User
from django.views.generic import View, CreateView, UpdateView
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
    success_url = reverse_lazy('blog:posts')
# Create your views here.


class UserLoginView(LoginView):
    template_name = 'accounts/form.html'
    next_page = reverse_lazy('blog:posts')


class UserLogoutView(LogoutView):
    next_page = '/blog/blogposts/'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'accounts/form.html'
    success_url = reverse_lazy('blog:posts')

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def user_profile(request, email):
    # 링크의 이메일을 db에서 찾음 // 없으면 404페이지
    user = get_object_or_404(User, email=email)

    # 로그인한 이메일과 링크의 이메일이 같은지 확인
    if request.user.email == user.email:
        context = {'profile_user': user}
        return render(request, 'accounts/profile.html', context)

    else:
        return HttpResponse('장난치지마라')

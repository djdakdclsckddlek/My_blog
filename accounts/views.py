from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import User
from django.views.generic import View, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
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
    next_page = '/accounts/login/'


class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'accounts/form.html'
    success_url = reverse_lazy('blog:posts')

    def get_object(self, queryset=None):
        return self.request.user

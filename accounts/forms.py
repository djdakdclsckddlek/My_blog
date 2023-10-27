from .models import User
from django import forms
from django.core.validators import MaxLengthValidator
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
# 직접 검증 클래스 validtors안에 포함시키기
# def my_validator(value):
#     if value in '!':
#         raise forms.ValidationError('!는 들어갈 수 없습니다.')
#     return value


# class SignupForm(forms.Form):
#     username = forms.CharField(
#         label='username',
#         max_length=20,
#         required=True,
#         validators=[
#             MaxLengthValidator(limit_value=20),
#             # my_validator,
#         ]
#     )
#     email = forms.CharField(
#         label='email',
#         max_length=50,
#         required=True,
#         validators=[
#             MaxLengthValidator(limit_value=50)
#         ]
#     )


# def clean_##   파라미터 검증
# def clean_username(self):
#     username = self.clean_data.get('username', None)
#     if username == None:
#         raise forms.ValidationError('이름은 필수값입니다.')
#     return username

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # settings에서 가르키고 있는 user모델
        model = get_user_model()
        fields = ['username', 'email']


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'profile_img', 'nickname', 'introduce']

    profile_img = forms.ImageField(required=False)
    nickname = forms.CharField(max_length=50, required=False)
    introduce = forms.CharField(max_length=200, required=False)
    password = None
    # password = forms.CharField(required=False, disabled=True)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['password'].widget = forms.HiddenInput()

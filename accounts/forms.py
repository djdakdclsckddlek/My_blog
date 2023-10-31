from .models import User
from django import forms
from django.core.validators import MaxLengthValidator
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
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
        fields = ['username', 'profile_img', 'nickname', 'introduce']

    profile_img = forms.ImageField(required=False)
    nickname = forms.CharField(max_length=50, required=False)
    introduce = forms.CharField(max_length=200, required=False)
    password = None
    # password = forms.CharField(required=False, disabled=True)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['password'].widget = forms.HiddenInput()


class CustomPasswordChangeForm(PasswordChangeForm):

    error_messages = {
        'password_incorrect': '기존 비밀번호가 일치하지 않습니다.',
        'password_mismatch': '비밀번호가 일치하지 않습니다.',
        'password_too_short': '비밀번호는 최소 8자 이상이어야 합니다.',
        'password_common': '비밀번호가 너무 흔해요. 다른 비밀번호를 사용해주세요.',
    }

    new_password1 = forms.CharField(
        label="새로운 비밀번호",
        widget=forms.PasswordInput(attrs={'placeholder': '새로운 비밀번호'}),
    )
    new_password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 확인'}),
    )

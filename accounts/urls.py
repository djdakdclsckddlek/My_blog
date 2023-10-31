from django.urls import path
from .views import SignupView, UserLoginView, UserLogoutView, UserUpdateView, user_profile, CustomPasswordChangeView
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'accounts'

urlpatterns = [
    path('signup/',  SignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('profile/', user_profile, name='profile'),
    path('update/change_password',
         CustomPasswordChangeView.as_view(), name='change_password'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

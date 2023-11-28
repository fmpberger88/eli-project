from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('impressum/', views.impressum, name='impressum'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('registration_confirmation/', views.registration_confirmation, name="registration_confirmation"),
    path('activate/<str:token>', views.activate, name="activate"),
]

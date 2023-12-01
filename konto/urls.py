from django.urls import path
from . import views

urlpatterns = [
    path('konto/', views.konto, name='konto'),
]

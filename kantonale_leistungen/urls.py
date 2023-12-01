from django.urls import path
from . import views

urlpatterns = [
    path('beihilfe/', views.beihilfe, name='beihilfe'),
    path('zuschuesse/', views.zuschuesse, name='zuschuesse'),
    path('betreuung_alter/', views.betreuung_alter, name='betreuung_alter'),
]
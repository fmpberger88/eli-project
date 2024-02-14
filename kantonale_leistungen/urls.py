from django.urls import path
from . import views

urlpatterns = [
    path('beihilfe/', views.beihilfe, name='beihilfe'),
    path('zuschuesse/', views.zuschuesse, name='zuschuesse'),
    path('betreuung_alter/', views.betreuung_alter, name='betreuung_alter'),

    # Ajax-Endpunkte
    path('gemeinde_data/', views.gemeinde_data, name='gemeinde_data'),
    path('leistungsanbietende_data/<int:gemeinde_id>/', views.leistungsanbietende_data, name='leistungsanbietende_data')
]

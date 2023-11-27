from django.urls import path
from .views import supplementary_benefits_info, eligibility_requirements, art_4_detail

urlpatterns = [
    path('supplementary_benefits_info/', supplementary_benefits_info, name='supplementary_benefits_info'),
    path('eligibility_requirements/', eligibility_requirements, name='eligibility_requirements'),
    path('art_4_detail/', art_4_detail, name='art_4_detail')
]

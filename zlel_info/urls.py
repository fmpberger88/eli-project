from django.urls import path
from .views import (supplementary_benefits_info,
                    eligibility_requirements,
                    art_4_detail,
                    art_5_detail,
                    art_6_detail,
                    art_7_detail,
                    art_8_detail,
                    art_9_detail,)

urlpatterns = [
    path('supplementary_benefits_info/', supplementary_benefits_info, name='supplementary_benefits_info'),
    path('eligibility_requirements/', eligibility_requirements, name='eligibility_requirements'),
    path('art_4_detail/', art_4_detail, name='art_4_detail'),
    path('art_5_detail/', art_5_detail, name='art_5_detail'),
    path('art_6_detail/', art_6_detail, name='art_6_detail'),
    path('art_7_detail/', art_7_detail, name='art_7_detail'),
    path('art_8_detail/', art_8_detail, name='art_8_detail'),
    path('art_9_detail/', art_9_detail, name='art_9_detail'),
]

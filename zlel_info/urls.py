from django.urls import path
from .views import (supplementary_benefits_info,
                    eligibility_requirements,
                    el_allgemein,
                    el_auslaender,
                    el_vermoegen,
                    el_einnahmen,
                    el_ausgaben,
                    el_kinder,
                    el_heim,
                    el_krankheit,
                    el_anmeldung)

urlpatterns = [
    path('supplementary_benefits_info/', supplementary_benefits_info, name='supplementary_benefits_info'),
    path('eligibility_requirements/', eligibility_requirements, name='eligibility_requirements'),
    path('el_allgemein/', el_allgemein, name='el_allgemein'),
    path('el_auslaender/', el_auslaender, name='el_auslaender'),
    path('el_vermoegen/', el_vermoegen, name='el_vermoegen'),
    path('el_einnahmen/', el_einnahmen, name='el_einnahmen'),
    path('el_ausgaben/', el_ausgaben, name='el_ausgaben'),
    path('el_kinder/', el_kinder, name='el_kinder'),
    path('el_heim', el_heim, name='el_heim'),
    path('el_krankheit', el_krankheit, name='el_krankheit'),
    path('el_anmeldung', el_anmeldung, name='el_anmeldung')
]

from django.shortcuts import render


# Create your views here.

def supplementary_benefits_info(request):
    return render(request, 'zlel_info/supplementary_benefits_info.html')


def eligibility_requirements(request):
    return render(request, 'zlel_info/eligibility_requirements.html')

def el_allgemein(request):
    return render(request, 'zlel_info/allgemein.html')

def el_auslaender(request):
    return render(request, 'zlel_info/auslaender.html')

def el_vermoegen(request):
    return render(request, 'zlel_info/vermoegen.html')

def el_einnahmen(request):
    return render(request, 'zlel_info/Einnahmen.html')

def el_ausgaben(request):
    return render(request, 'zlel_info/Ausgaben.html')

def el_kinder(request):
    return render(request, 'zlel_info/Kinder.html')

def el_krankheit(request):
    return render(request, 'zlel_info/krankheit.html')

def el_heim(request):
    return render(request, 'zlel_info/heim.html')

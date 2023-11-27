from django.shortcuts import render


# Create your views here.

def supplementary_benefits_info(request):
    return render(request, 'zlel_info/supplementary_benefits_info.html')


def eligibility_requirements(request):
    return render(request, 'zlel_info/eligibility_requirements.html')

def art_4_detail(request):
    return render(request, 'zlel_info/Art4Detail.html')
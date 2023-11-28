from django.shortcuts import render


# Create your views here.

def supplementary_benefits_info(request):
    return render(request, 'zlel_info/supplementary_benefits_info.html')


def eligibility_requirements(request):
    return render(request, 'zlel_info/eligibility_requirements.html')

def art_4_detail(request):
    return render(request, 'zlel_info/allgemein.html')

def art_5_detail(request):
    return render(request, 'zlel_info/auslaender.html')

def art_6_detail(request):
    return render(request, 'zlel_info/vermoegen.html')

def art_7_detail(request):
    return render(request, 'zlel_info/Art7Detail.html')

def art_8_detail(request):
    return render(request, 'zlel_info/Art8Detail.html')

def art_9_detail(request):
    return render(request, 'zlel_info/Art9Detail.html')

def art_10_detail(request):
    return render(request, 'zlel_info/Art10Detail.html')

def art_11_detail(request):
    return render(request, 'zlel_info/Art11Detail.html')

def art_12_detail(request):
    return render(request, 'zlel_info/Art12Detail.html')

def art_13_detail(request):
    return render(request, 'zlel_info/Art13Detail.html')

def art_14_detail(request):
    return render(request, 'zlel_info/Art14Detail.html')

def art_15_detail(request):
    return render(request, 'zlel_info/Art15Detail.html')

def art_16_detail(request):
    return render(request, 'zlel_info/Art16Detail.html')
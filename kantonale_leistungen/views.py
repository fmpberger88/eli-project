from django.shortcuts import render

# Create your views here.
def beihilfe(request):
    return render(request, 'kantonale_leistungen/beihilfe.html')

def zuschuesse(request):
    return render(request, 'kantonale_leistungen/zuschuesse.html')

def betreuung_alter(request):
    return render(request, 'kantonale_leistungen/betreuung_alter.html')
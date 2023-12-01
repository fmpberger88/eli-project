from django.shortcuts import render

# Create your views here.
def konto(request):
    return render(request, 'konto/konto.html')

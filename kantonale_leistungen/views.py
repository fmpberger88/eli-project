from django.shortcuts import render
from django.http import JsonResponse
from .models import Gemeinde, Leistungsanbietende


# Create your views here.
def beihilfe(request):
    return render(request, 'kantonale_leistungen/beihilfe.html')


def zuschuesse(request):
    return render(request, 'kantonale_leistungen/zuschuesse.html')


def betreuung_alter(request):
    return render(request, 'kantonale_leistungen/betreuung_alter.html')


def gemeinde_data(request):
    data = list(Gemeinde.objects.values('id', 'name'))
    return JsonResponse(data, safe=False)


def leistungsanbietende_data(request, gemeinde_id):
    data = list(
        Leistungsanbietende.objects.filter(gemeinde__id=gemeinde_id).values("id", "name", "taetigkeit", "beschreibung",
                                                                            "leistung", "internetlink"))
    return JsonResponse(data, safe=False)

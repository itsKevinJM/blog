from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def utilisateurs_view(request):
    # return HttpResponse("Page d'utilisateurs")
    return render(request, 'utilisateurs/liste.html')


def creer_view(request):
    return HttpResponse('page création utilisateur')

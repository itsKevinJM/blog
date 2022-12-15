from django.http import HttpResponse


def home_view(request):
    return HttpResponse('hello world !')


def contact_view(request):
    return HttpResponse('Contactez nous !')

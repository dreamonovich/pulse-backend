from django.http import HttpResponse


def ping_view(request):
    return HttpResponse('ok')

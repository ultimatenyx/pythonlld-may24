from django.http import HttpResponse, HttpRequest

def users(request: HttpRequest)->HttpResponse:
    return HttpResponse("Hello, users!")
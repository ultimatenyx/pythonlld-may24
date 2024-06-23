from django.http import HttpResponse


def helloCloudView(request):
    return HttpResponse('Hello Cloud!')
from django.http import HttpResponse,HttpRequest

def say_hello(request):
    return HttpResponse('Hello from the World of awesome!')

def say_hello_with_name(request,name):
    print(request.headers)
    return HttpResponse('Hello, Mr %s from the World of awesome!' % name)
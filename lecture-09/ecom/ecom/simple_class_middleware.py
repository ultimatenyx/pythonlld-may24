from django.http import HttpResponse


class SimpleClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Class based before")
        response = self.get_response(request)

        print("Class based after")
        return response

    def process_exception(self, request, exception):
        print("Exception")
        print(str(exception))
        return HttpResponse("This is empty")
class SimpleClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Class based before")
        response = self.get_response(request)

        print("Class based after")
        return response

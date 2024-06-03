def simple_middleware(get_response):
    def middleware(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response

    return middleware

def another_middleware(get_response):
    def middleware(request):
        print("This is before another middleware view")
        response = get_response(request)
        print("This is after another middleware view")
        return response
    return middleware
from django.shortcuts import redirect

class BlockAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path in ['/home/', '/register/']:
            return redirect('/login/')
        
        response = self.get_response(request)
        return response

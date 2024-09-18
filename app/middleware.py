# myapp/middleware.py
class PreviousUrlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Save the current URL in session
        if 'prev_url' in request.session:
            request.session['previous_url'] = request.session['prev_url']
        request.session['prev_url'] = request.build_absolute_uri()
        
        response = self.get_response(request)
        return response

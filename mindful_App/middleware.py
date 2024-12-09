from django.shortcuts import redirect

class RedirectHTMLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If the path ends with '.html', remove it and redirect
        if request.path.endswith('.html'):
            clean_path = request.path[:-5]  # Remove '.html'
            return redirect(clean_path)
        return self.get_response(request)

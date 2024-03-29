class SecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Strict-Transport-Security
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'

        # Content-Security-Policy
        csp = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdn.jsdelivr.net; "
            "img-src 'self' data:; "  # Allow images from same origin and data URLs
            "object-src 'none';"
        )
        response['Content-Security-Policy'] = csp

        # Permissions-Policy
        response['Permissions-Policy'] = 'geolocation=(self), microphone=()'

        return response

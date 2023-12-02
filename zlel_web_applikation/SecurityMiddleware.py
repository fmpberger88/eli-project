class SecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Strict-Transport-Security
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'

        # Content-Security-Policy
        # Ermöglicht das Laden von Stilen von Google Fonts und Bootstrap CDN
        csp = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdn.jsdelivr.net; "
            "object-src 'none';"
        )
        response['Content-Security-Policy'] = csp

        # Permissions-Policy
        response['Permissions-Policy'] = 'geolocation=(self), microphone=()'

        return response

class SecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Strict-Transport-Security
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'

        # Content-Security-Policy
        # Customize this policy based on your needs
        response['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; object-src 'none';"

        # Permissions-Policy
        # You need to customize this according to the APIs you need
        response['Permissions-Policy'] = 'geolocation=(self), microphone=()'

        return response

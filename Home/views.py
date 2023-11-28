from django.core.signing import BadSignature, SignatureExpired, dumps, loads
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomerUserCreationForm  # Import the custom form
from django.http import HttpResponse
from django.contrib.auth.models import User



class SignUp(CreateView):
    form_class = CustomerUserCreationForm
    success_url = reverse_lazy("registration_confirmation")
    template_name = "registration/registration.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()

        # Generate a token
        token = dumps(user.pk)

        # Email content
        subject = "Activate your Account"
        message = render_to_string('registration/activation_email.html', {
            'user': user,
            'token': token
        })

        # Send email
        send_mail(subject, message, None, [user.email])

        return response


def activate(request, token):
    try:
        user_pk = loads(token, max_age=86400)  # Token expires in 1 day
    except (BadSignature, SignatureExpired):
        return HttpResponse('Aktivierungslink ist ungültig oder abgelaufen')

    user = User.objects.get(pk=user_pk)
    user.is_active = True
    user.save()

    return HttpResponse('Dein Konto wurde aktiviert')


def home(request):
    return render(request, 'home/index.html')

def impressum(request):
    return render(request, 'home/impressum.html')

def registration_confirmation(request):
    return render(request, 'registration/registration_confirmation.html')

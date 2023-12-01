from django.core.signing import BadSignature, SignatureExpired, dumps, loads
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomerUserCreationForm  # Import the custom form
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse



class SignUp(CreateView):
    form_class = CustomerUserCreationForm
    success_url = reverse_lazy("registration_confirmation")
    template_name = "registration/registration.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        # Get the current site
        current_site = get_current_site(self.request)
        # Get the domain name
        domain = current_site.domain
        # Generate a token
        token = dumps(user.pk)
        # Generate activation link
        activation_link = 'http://{domain}{path}'.format(
            domain=domain,
            path=reverse('activate', kwargs={'token': token})
        )

        context = {
            'user': user,
            'activation_link': activation_link
        }

        # Email content
        subject = "Activate your Account"
        message = render_to_string('registration/activation_email.txt', context)  # Text version
        html_message = render_to_string('registration/activation_email.html', context)  # HTML version

        # Send email
        send_mail(subject, message, None, [user.email], html_message=html_message)

        return response


def activate(request, token):
    try:
        user_pk = loads(token, max_age=86400)  # Token expires in 1 day
    except (BadSignature, SignatureExpired):
        return HttpResponse('Aktivierungslink ist ungültig oder abgelaufen')

    user = User.objects.get(pk=user_pk)
    user.is_active = True
    user.save()

    # Redirect to the account activated page
    return render(request, 'registration/account_activated.html')


def home(request):
    return render(request, 'home/index.html')

def impressum(request):
    return render(request, 'home/impressum.html')

def registration_confirmation(request):
    return render(request, 'registration/registration_confirmation.html')

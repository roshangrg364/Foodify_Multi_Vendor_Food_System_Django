from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings


def getdashboardurl(user):
    if user.role == 1:
        dashboardurl = "vendordashboard"
    elif user.role == 2:
        dashboardurl = "customerdashboard"
    elif user.role is None and user.is_superadmin:
        dashboardurl = "/admin-panel"

    return dashboardurl


def send_verification_email(request, user, subject, templatePath):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    mail_subject = subject
    message = render_to_string(
        templatePath,
        {
            "user": user,
            "domain": current_site,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": default_token_generator.make_token(user),
        },
    )

    to_email = user.email
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.content_subtype = "html"
    mail.send()


def send_notification(subject, template, data, to_emailAddress=None):
    from_email = settings.DEFAULT_FROM_EMAIL
    mail_subject = subject
    message = render_to_string(template, data)

    to_email = data["user"].email
    if to_emailAddress is not None:
        to_email = to_emailAddress
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.content_subtype = "html"
    mail.send()

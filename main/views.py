"""Views for main app."""

from django.views.generic import TemplateView

from utils.views import UserLoggedInRedirectMixin


class LandingPage(TemplateView):

    """Landing page view."""

    template_name = 'main/landing_page.html'

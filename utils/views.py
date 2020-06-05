"""Views utils."""

from django.shortcuts import redirect


class UserLoggedInRedirectMixin:

    """Mixin that redirects the user to a given view if the user is logged in."""

    redirect_url = 'dashboard'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.redirect_url)
        return super().dispatch(*args, **kwargs)

class LoginRequiredMixin:

    """Mixin that redirects the user to a given view if the user is not logged in."""

    redirect_url = 'landing_page'

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(self.redirect_url)
        return super().dispatch(*args, **kwargs)

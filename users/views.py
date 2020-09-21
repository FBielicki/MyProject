"""Views for users app."""
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import (
    PasswordChangeView as BasePasswordChangeView,
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView,
)
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from utils.views import UserLoggedInRedirectMixin, LoginRequiredMixin
from .forms import LoginForm, RegistrationForm, TeacherForm, ChangeForm
from django.views import View
from django.views.generic import TemplateView
from users.forms import (
    LoginForm,
    RegistrationForm,
    TeacherForm,
    ChangePasswordForm,
)
from courses.models import ScheduleChange
from courses.models import Teacher

from utils.views import (
    LoginRequiredMixin,
    UserLoggedInRedirectMixin,
)


class RegistrationView(UserLoggedInRedirectMixin, View):

    """Registration view."""

    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        return render(request, 'users/registration.html', context={
            'form': RegistrationForm()
        })

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.save(commit=False)

            # instant login after registraion
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

            # Registration Email Content
            subject = 'Thank you for your Registration ;)'
            message = 'Hi ' + data.first_name + '! \n Your Registration was Successful! \n Thanks! ;)'
            from_email = settings.EMAIL_HOST_USER
            to_list = [data.email]

            # send mail
            send_mail(subject, message, from_email, to_list, fail_silently=False)

            login(request, new_user)
            return redirect('login')
        else:
            return render(request, 'users/registration.html', context={
                'form': form
            })


class LoginView(UserLoggedInRedirectMixin, BaseLoginView):

    """Login view."""

    form_class = LoginForm
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, BaseLogoutView):

    """Logout view."""

    next_page = 'landing_page'


class DashboardView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/dashboard.html')


class TeacherView(LoginRequiredMixin, View):

    """Teacher view."""

    def get(self, request, *args, **kwargs):
        return render(request, 'users/teachers.html', context={
            'form': TeacherForm(instance=request.user)
        })

    def post(self, request, *args, **kwargs):
        form = TeacherForm(instance=request.user, data=request.POST)
        teacher = Teacher.objects.all()
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return render(request, 'users/teachers.html', context={
                'form': form, 'teachers': teacher
            })


class ChangeView(LoginRequiredMixin, View):

    """Change view."""

    form_class = ChangeForm

    def get(self, request, *args, **kwargs):
        return render(request, 'users/edit.html', context={
            'form': ChangeForm(instance=request.user)
        })

    def post(self, request, *args, **kwargs):
        form = ChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
        else:
            return render(request, 'users/edit.html', context={
                'form': form
            })


class ChangePasswordView(LoginRequiredMixin, BasePasswordChangeView):

    """Change Password view."""

    success_url = '/dashboard'
    form_class = ChangePasswordForm
    template_name = 'users/change_password.html'


class ScheduleView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        change = ScheduleChange.objects.all()
        return render(request, 'users/schedule.html', context={'change': change})


class SendScheduleView(LoginRequiredMixin, View):

    """Test view to send Schedule Change data per Email."""

    def get(self, request, *args, **kwargs):

        subject = 'Daily Schedule Change'
        changes = ScheduleChange.objects.filter(teacher__in=request.user.courses.all())
        c = []

        for i in changes:
            c.append(str(i.teacher.last_name) + ": ")
            c.append(str(i.absent_from) + "-" + str(i.absent_to))
            c.append('Type: ' + i.type)
            if i.new_classroom != None:
                c.append('New Classroom: ' + i.new_classroom)
            if i.new_teacher != None:
                c.append('New Teacher: ' + i.new_teacher)
            if i.additional_text != None:
                c.append('Additional Text: ' + i.additional_text)
            c.append("\n")

        message = 'Hi! \n here are your Daily Schedule Changes ;) \n \n' + str("   ".join(c))
        from_email = settings.EMAIL_HOST_USER
        to_list = [request.user.email]

        send_mail(subject, message, from_email, to_list, fail_silently=False)

        return render(request, 'users/schedule.html')

class HelpView(TemplateView):

    template_name = 'users/help.html'
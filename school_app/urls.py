from django.contrib import admin
from django.urls import path

from main.views import LandingPage
from users.views import (
    ChangeView,
    LoginView,
    LogoutView,
    RegistrationView,
    DashboardView,
    TeacherView,
    ChangePasswordView,
    ScheduleView,
    SendScheduleView
)

# all accasable urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('', LandingPage.as_view(), name='landing_page'),
    path('teachers/', TeacherView.as_view(), name='teachers'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('edit/', ChangeView.as_view(), name='edit'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('send_schedule/', SendScheduleView.as_view())
]

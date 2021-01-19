from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth

routes = [
    (r'home/', views.home, 'home'),
    (r'about/', views.about, 'about'),
    (r'contact/', views.contact, 'contact'),
    (r'homeX/', TemplateView.as_view(template_name='index.html'), 'homex'),
    (r'profile/',views.ProfileView.as_view(),'profile'),
    # for login auth via django pre apps
    (r'accounts/login', auth.LoginView.as_view(template_name="accounts/login.html"), 'login'),
    (r'accounts/logout', auth.LogoutView.as_view(template_name="home.html"), 'logout'),
]

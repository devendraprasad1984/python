from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth
routes=[
    (r'home/',views.home,'home'),
    (r'about/',views.about,'about'),
    (r'contact/',views.contact,'contact'),
    (r'homeX/',TemplateView.as_view(template_name='index.html'),'homex'),
    #for login auth via django pre apps
    (r'accounts/login',auth.LoginView.as_view(template_name="accounts/login.html"),'login'),
]

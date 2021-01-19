from . import views
from django.views.generic.base import TemplateView

routes=[
    (r'home/',views.home,'home'),
    (r'about/',views.about,'about'),
    (r'contact/',views.contact,'contact'),
    (r'homeX/',TemplateView.as_view(template_name='index.html'),'homex'),
]

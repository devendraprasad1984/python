from . import views
from django.views.generic.base import TemplateView

routes=[
    (r'home/',views.home),
    (r'about/',views.about),
    (r'contact/',views.contact),
    (r'homeX/',TemplateView.as_view(template_name='index.html')),
]

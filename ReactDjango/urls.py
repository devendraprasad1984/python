from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView
from website import webroutes

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('api/',  include('api.urls')),
    path('auth/',  obtain_auth_token),
]

# this url pattern works when you hit localhost:8000/home
appRoutes=[webroutes.routes]
for route in appRoutes:
    for x in route:
        urlpatterns.append(path(x[0], x[1],name=x[2]))

# auto configure auth views
# path('accounts/', include('django.contrib.auth.urls'))

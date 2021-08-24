"""loan_payments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


# from rest_framework_swagger.views import get_swagger_view
# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


# schema_view = get_swagger_view(title='GeekTrust Ledger.co API docs')
# schema_view = get_schema_view(title='GeekTrust Ledger.co API docs', renderer_classes=[CoreJSONRenderer])
schema_view = get_schema_view(
    openapi.Info(
        title="Geek Trust Ledger.co API",
        default_version='v1',
        description="geek trust description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('banks/', include("bank_manager.urls")),
    path('customers/', include("customer_manager.urls")),
    path('onboard/', include("subscribe.urls")),
    path('loans/', include("loan_manager.urls")),
    # path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='drf_yasg_swagger'),
    # path('^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # url('apis/', schema_view),
    # url(r'^', schema_view, name="docs"),
    # url('swagger/', TemplateView.as_view(
    #     template_name='swagger.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='swagger'),
]

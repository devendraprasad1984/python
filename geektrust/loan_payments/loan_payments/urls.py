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
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='GeekTrust Ledge.co API docs')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('onboard/', include("subscribe.urls")),
    path('loans/', include("loan_manager.urls")),
    path('banks/', include("bank_manager.urls")),
    path('customers/', include("customer_manager.urls")),
    path('apis/', schema_view),
]

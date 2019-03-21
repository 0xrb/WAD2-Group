"""ratemydog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from django.contrib.auth.views import LoginView
from django.conf.urls import url

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('', include('bestboy.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('dog/', include('bestboy.urls')),
    path('profile/', include('bestboy.urls'))
    #url(r'^(?P<username>\w+)/', include('bestboy.urls')),
    #url(r'^(?P<dogid>\w+)/', include('bestboy.urls')),
]

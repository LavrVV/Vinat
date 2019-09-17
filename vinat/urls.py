"""vinat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from vinat import settings

from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view()),
    path('ps', views.PSView.as_view()),
    path('pvd', views.PVDView.as_view()),
    path('pp', views.PPView.as_view()),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
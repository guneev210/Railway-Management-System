"""Project_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from railway import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('signup/', views.signup),
   path('login/', views.login_user),
   path('', views.home),    
   path('logout/', views.logout_user),
   path('traininfo/', views.traininfo),
   path('findtrains/', views.findtrains),
   path('ticket/', views.ticket),
]

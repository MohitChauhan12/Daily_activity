"""
URL configuration for dailyactivities project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from activities import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login, name="login"),
    path("registration/", views.registration, name="registration"),
    path("welcome/", views.welcome, name="welcome"),
    path("insert/", views.insertData, name="insertData"),
    path('update/<id>',views.updateData,name='updateData'),
    path('delete/<id>',views.deleteData,name='deleteData'),
    path("",views.logout,name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

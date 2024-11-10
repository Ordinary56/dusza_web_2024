"""
URL configuration for dusza_project_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.contrib.auth.views import LogoutView
from dusza_app import views 

urlpatterns = [
    path("", views.login, name="login"),
    path("team/", views.TeamView, name="team"),
    path("modify/", views.modify, name="modify"),
    path("organizer/", views.OrganizerView, name="organizer"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("create/", views.create, name="create"),
    path("school/", views.SchoolView, name="school"),
    path("delete/", views.delete,name="delete"),
    path("export/", views.export,name="export")
]

if settings.DEBUG:
    urlpatterns += [
        path('admin/', admin.site.urls),
    ]

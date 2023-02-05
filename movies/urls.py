"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from movies_app.views import (
    get_homepage,
    h1_exercise,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("movies_app.urls")),
    path("", get_homepage),
    path("h1", h1_exercise),
    # path("h1/ex1", h1_exercise_ex1),
    # path("h1/ex2", h1_exercise_ex2),
    # path("h1/ex3", h1_exercise_ex3),
]

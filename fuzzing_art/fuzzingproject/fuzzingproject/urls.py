"""fuzzingproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from userapp import views as uv
from categoryapp import views as cv
from mypageapp import views as mv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cv.home, name='home'),
    path('signup/',uv.signup, name='signup'),
    path('login/',uv.login, name='login'),
    path('logout/',uv.logout, name='logout'),
    path('mypage/', mv.mypage, name='mypage')
]

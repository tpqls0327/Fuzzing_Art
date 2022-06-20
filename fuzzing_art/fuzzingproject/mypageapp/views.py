# 퍼징아트 마이페이지
from django.shortcuts import render
from userapp.models import AccountUser as au

# Create your views here.

def mypage(request):
    user = request.user
    myuser = au.objects.get(user=user)

    return render(request, 'mypage.html', {'myuser': myuser})
    {'main_food' : Main_Food}
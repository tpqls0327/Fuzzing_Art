# 퍼징아트 회원가입,로그인 페이지
from django.shortcuts import render, redirect
from .models import AccountUser
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render
from django.core import serializers

# Create your views here.
ERROR_MSG = {
    'ID_EXIST': '이미 사용 중인 아이디 입니다.',
    'ID_NOT_EXIST': '존재하지 않는 아이디 입니다',
    'ID_PW_MISSING': '아이디와 비밀번호를 다시 확인해주세요.',
    'PW_CHECK': '비밀번호가 일치하지 않습니다.',
}

def login(request):
    context = {
        'error': {
            'state': False,
            'msg': ''
        }
    }

    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        print('hello')

        user = User.objects.filter(username=user_id)

        if (user_id and user_pw):
            if len(user) != 0:
                user = auth.authenticate(
                    username=user_id,
                    password=user_pw
                )
                if user != None:
                    auth.login(request, user)

                    return redirect('home')
                else:
                    context['error']['state'] = True
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
            else:
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['ID_NOT_EXIST']
        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']

    # return render(request, 'login.html', context)
    # return JsonResponse({
    #     'message' : '안녕 파이썬 장고',
    #     'items' : ['파이썬', '장고', 'AWS', 'Azure'],
    # }, json_dumps_params={'ensure_ascii': True})
    # posts = AccountUser.objects.filter(name='test')
    # post_list = serializers.serialize('json', posts)
    # return HttpResponse(post_list, content_type="text/json-comment-filtered")
    dummy_data = {
            'text' : '텍스트입니다'
        }
    return JsonResponse(dummy_data)

def signup(request):
    context = {
        'error': {
            'state': False,
            'msg': ''
        }
    }

    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_pw_check = request.POST['user_pw_check']
        user_email = request.POST['user_email']
        # add
        user_name = request.POST['user_name']
        user_nickname = request.POST['user_nickname']
        user_gender = request.POST['user_gender']
        user_age = request.POST['user_age']
        user_address = request.POST['user_address']

        if (user_id and user_pw):
            user = User.objects.filter(username=user_id)
            if len(user) == 0:
                if (user_pw == user_pw_check):
                    created_user = User.objects.create_user(
                        username=user_id,
                        password=user_pw,
                        email=user_email
                    )                   
                    # add
                    AccountUser.objects.create(
                        user = created_user,
                        name = user_name,
                        nickname = user_nickname,
                        gender = user_gender,
                        age = user_age,
                        address = user_address
                    )

                    auth.login(request, created_user)
                    return redirect('home')
                else:
                    context['error']['state'] = True
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
            else:
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['ID_EXIST']
        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']

    return render(request, 'signup.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')

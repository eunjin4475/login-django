from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

import json


def login(request):
    user_data = {
        'username': 'python',
        'password': 'django'
    }
    # """ 
    # #username과 password에 대한 입력이 없다면
    # if username is None and password is None:
    # return render(request, 'users/login.html')
    # #username과 password 중 하나의 입력이 누락되었을 떄
    # elif username is None or password is None:
    # return HttpResponse('불가능한 접근입니다.')
    # #blank상태일 때는 유저가 input을 입력하지 않고 제출했을 때(유저의 실수)
    # if username == '':
    # return HttpResponse('유저 아이디를 입력해주세요')
    # if password == '':
    # return HttpResponse('유저 비밀번호를 입력해주세요')
    
    # """
    if(request.method == 'GET'):
        username = request.GET['username']
        password = request.GET['password']
        # """if username is None:
        #     return HttpResponse('유저 아이디를 입력해주세요.')
        # fi password is None:
        # return HttpResponse('유저 비밀번호를 입력해주세요.')"""

        if (username !=user_data['username']):
            return HttpResponse('유저 아이디가 올바르지 않습니다.')
        if (password != user_data['password']):
            return HttpResponse('유저 비밀번호가 올바르지 않습니다.')

        return HttpResponse('로그인 성공!!')
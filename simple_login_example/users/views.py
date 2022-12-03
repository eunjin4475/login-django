# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse

import json
def login(request):
    user_data = {
        'username': 'python',
        'password': 'django'
    }
 
    context = {
        'method' : request.method,
        'is_vaild': True
    }

    if (request.method == 'GET'):
        return render(request, 'users/login.html', context)

    if(request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            #username과 password 중 하나의 입력이 누락되었을 떄
            # elif username is None or password is None:
            #     return HttpResponse('불가능한 접근입니다.')


            #blank상태일 때는 유저가 input을 입력하지 않고 제출했을 때(유저의 실수)
            if username == '':
                context['is_vaild'] = False
            if password == '':
                context['is_vaild'] = False

            if (username !=user_data['username']):
                context['is_vaild'] = False
            if (password != user_data['password']):
                context['is_vaild'] = False

            if context['is_vaild']:
                response = redirect('pages:index')

                response.set_cookies('username', user_data['username'])
                response.set_cookies('password', user_data['password'])
                response.set_cookies('is_login', True)

                return response
            return render(request, 'users/login.html', context)
def login_detail(request, id):
    return HttpResponse('user id는 + str(id') + '입니다.')

def index(request):
    return render(request, 'index.html')

def logout(request):
    response = redirect('pages:index')
    response.delete_cookie('is_login')
    response.delete_cookie('username')
    response.delete_cookie('password')

    return response

            
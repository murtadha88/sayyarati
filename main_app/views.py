from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

class Login(LoginView):
    template_name = 'login.html'


def home(request):
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')


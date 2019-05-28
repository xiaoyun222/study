#coding:utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from hosts import models
from hosts import formg
from hosts import formss
# Create your views here.

def hello(request):
    return HttpResponse('hello test')
def keke(reuqest):
    return HttpResponse('keke')

def show(request):
    obj = models.device.objects.values()
    return render(request, 'detail.html',{'msg_data':obj, 'user':'henry'})

def login(reqeust):
    objform = formg.loginform()
    return render_to_response('login.html',{'data':'objform', 'user':'alexsb'})

def userlist(request):
    obj = formss.UserInfo()
    





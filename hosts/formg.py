#coding:utf-8
from django import forms

class loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField()



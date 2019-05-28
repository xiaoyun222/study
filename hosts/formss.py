#coding:uft-8

from django import forms

class UserInfo(forms.Form):
    email = forms.EmailField()
    host = forms.CharField()
    port = forms.CharField()
    mobile = forms.CharField

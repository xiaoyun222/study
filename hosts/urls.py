from django.conf.urls import url, include
from hosts.views import hello,show, login, keke


urlpatterns = [
    url(r'^hello/', hello),
    url(r'^show/', show),
    url(r'^login/', login),
    url(r'^keke/', keke),

]

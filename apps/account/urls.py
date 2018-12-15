from django.conf.urls import url
from django.contrib.auth import login

# from apps.account import views
from django.urls import include

from apps.account import views

app_name = 'accounts'

urlpatterns = [
    #url(r'^login/$', views.login_usuario, name='login'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^registrar/$', views.register, name='registrar'),
    url(r'^editar/$', views.edit, name='editar'),
]
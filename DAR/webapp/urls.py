from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name=""),
  path('login', views.login, name="login"),
  path('userlogout',views.userlogout,name='userlogout'),
  path('register', views.register, name="register"),
]
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name=""),
  path('login', views.login, name="login"),
  path('userlogout',views.userlogout,name='userlogout'),
  path('register', views.register, name="register"),
  path('add_property', views.add_property, name="add_property"),
  path('jdata',views.jdata,name='jdata'),
]
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name=""),
  path('login', views.login, name="login"),
  path('userlogout',views.userlogout,name='userlogout'),
  path('register', views.register, name="register"),
  path('add_property', views.add_property, name="add_property"),
  path('jdata',views.jdata,name='jdata'),
  path('update_property/<int:property_id>', views.update_property, name="update_property"),
  path('settings', views.settings, name="settings"),
  path('property_information', views.property_information, name="property_information")
  
  
]
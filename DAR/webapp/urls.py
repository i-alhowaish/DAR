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
  # path('property_information', views.property_information, name="property_information"),
  path('property_information/<int:pid>', views.property_information, name='property_information'),
  path('add_to_favorite/<int:pid>', views.add_to_favorite, name='add_to_favorite'),
  path('search', views.search, name='search'),
  path('profile', views.profile, name='profile'),  # just for testing(if the page work or not) you can change it
  path('favorate', views.favorate, name='favorate'),  # just for testing(if the page work or not) you can change it
]
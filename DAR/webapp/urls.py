from django.urls import path
from . import views

from django.urls import path
from .views import add_to_favorite, remove_from_favorite

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
  # path('profile', views.profile, name='profile'),# just for testing(if the page work or not) you can change it
  path('profile/<str:username>/', views.profile, name='profile'),
  # path('favorate', views.favorate, name='favorate'),  # just for testing(if the page work or not) you can change it
  path('favorite/', views.favorites, name='favorite'),
  path('dashboard', views.dashboard, name='dashboard'),  # just for testing(if the page work or not) you can change it
  path('remove-from-favorite/<int:pid>/', views.remove_from_favorite, name='remove-from-favorite'),
  path('delete_property/<int:pid>', views.delete_property, name='delete_property'),
  path('my_properties/', views.my_properties, name='my_properties')

]
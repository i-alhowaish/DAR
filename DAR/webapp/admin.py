from django.contrib import admin
from .models import *

# class useradmin(admin.ModelAdmin):
#     list_display=()
class PropertyAdmin(admin.ModelAdmin):
    list_display=('description', 'type', 'price', 'furnished', 'number_of_bathrooms', 'region', 'city', 'street', 
                  'neighborhood', 'length', 'width', 'number_of_sides', 'number_of_rooms', 
                  'sell_or_rent', 'number_of_parkings', 'number_of_bedrooms', 'year_built','lng','lat')
class PropertyImagesAdmin(admin.ModelAdmin):
    list_display=('image','property')
class PropertyImages360Admin(admin.ModelAdmin):
    list_display=('image360','property360')
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','phone_number','color')
class ProfileFavorite(admin.ModelAdmin):
    list_display=('property','uid')
class ProfileReport(admin.ModelAdmin):
    list_display=('property','uid','description','date')



# # Register your models here.
admin.site.register(Favorite,ProfileFavorite)
admin.site.register(Report,ProfileReport)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Property,PropertyAdmin)
admin.site.register(PropertyImages,PropertyImagesAdmin)
admin.site.register(PropertyImages360,PropertyImages360Admin)


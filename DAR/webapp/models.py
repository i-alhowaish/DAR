from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from . import locations



REGION_CHOICES = locations.load_choices_from_json('locationsJSON/regions_lite.json', 'name_ar', 'name_ar')
CITY_CHOICES = locations.load_choices_from_json('locationsJSON/cities_lite.json', 'name_ar', 'name_ar')
NEIGHBORHOOD_CHOICES = locations.load_choices_from_json('locationsJSON/districts_lite.json', 'name_ar', 'name_ar')




# Create your models here.
# class Course(models.Model):
#     name =  models.CharField(max_length=70)
#     instructor=models.CharField(max_length=70)
#     courseid = models.CharField(max_length=30)
#     hours = models.IntegerField()
#     hostcollege = models.ForeignKey(College, on_delete=models.CASCADE, related_name="courses")
#     dicription=models.CharField(max_length=300)


#     def str(self):
#         return f"course info are name: {self.name} ,id: {self.courseid} , credit Hours: {self.hours} ,Host college : {self.hostcollege}"


# class user(models.Model):
#     us = models.OneToOneField(User,on_delete=models.CASCADE)
    # uid = models.AutoField(primary_key=True)
    # fname = models.CharField(max_length=100)
    # lname = models.CharField(max_length=100)
    # email = models.EmailField(unique=True)
    # password = models.CharField(max_length=100)

    # django user has these attributes ^
    # phone_number = models.CharField(max_length=15)
    # so we might add it later on
    #logo = models.ImageField(upload_to='subscription_logos/')
    

# class Property(models.Model):
#     pid = models.AutoField(primary_key=True)
#     uid = models.ForeignKey(User, on_delete=models.CASCADE)
#     description = models.TextField()
#     type = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     furnished = models.BooleanField()
#     number_of_bathrooms = models.IntegerField()
#     region = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     street = models.CharField(max_length=100)
#     neighborhood = models.CharField(max_length=100)
#     coordinate = models.CharField(max_length=100) # Or use a GIS field for geographic coordinates
#     length = models.DecimalField(max_digits=10, decimal_places=2)
#     width = models.DecimalField(max_digits=10, decimal_places=2)
#     number_of_sides = models.IntegerField()
#     facade = models.CharField(max_length=100)
#     number_of_rooms = models.IntegerField()
#     sell_or_rent = models.CharField(max_length=50)
#     number_of_parkings = models.IntegerField()
#     number_of_bedrooms = models.IntegerField()
#     year_built = models.IntegerField()
class Property(models.Model):
    pid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    Type_Choices=[
        ('Apartment','شقة'),
        ('House','فلة'),
        ('Farm','مزرعة'),
        ('Floor','دور'),
        ('Istrahah','استراحة'),
        ('Land','أرض')
          ]
    type = models.CharField(max_length=100,choices=Type_Choices)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    furnished = models.BooleanField()
    number_of_bathrooms = models.IntegerField(null=True, blank=True)
    
    region = models.CharField(max_length=100, choices=REGION_CHOICES)
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    street = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100, choices=NEIGHBORHOOD_CHOICES)
    coordinate = models.CharField(max_length=100, blank=True, null=True)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_sides = models.IntegerField(null=True, blank=True)
    # facade = models.CharField(max_length=100, blank=True, null=True)
    number_of_rooms = models.IntegerField(null=True, blank=True)
    SELL_OR_RENT_CHOICES = [
        ('sell', 'بيع'),
        ('rent', 'اجار'),
    ]
    sell_or_rent = models.CharField(max_length=50, choices=SELL_OR_RENT_CHOICES)
    number_of_parkings = models.IntegerField(null=True, blank=True)
    number_of_bedrooms = models.IntegerField(null=True, blank=True)
    year_built = models.IntegerField(null=True, blank=True)

class PropertyImages(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

class Report(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()

class Favorite(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

class Contact(models.Model):
    fid = models.AutoField(primary_key=True)
    message = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True)

class RealEstateTransactions(models.Model):
    tid = models.AutoField(primary_key=True)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    date = models.DateField()
    classification = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    number_of_properties = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)

class Subscription(models.Model):
    sid = models.AutoField(primary_key=True)
    duration = models.IntegerField()
    
    
class PropertyImages360(models.Model):
    property360 = models.ForeignKey(Property, related_name='images360', on_delete=models.CASCADE)
    image360 = models.ImageField(upload_to='property_images360/')

    
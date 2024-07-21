from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class

# CarModelAdmin class
# class CarModelAdmin(models.ModelAdmin):
#     fields = ['car_make', 'name', 'type' 'year']

# CarMakeAdmin class with CarModelInline
# class CarMakeAdmin(models.ModelAdmin):
#     fields = ['name', 'description']

# Register models here
# admin.site.register(CarModel, CarModelAdmin)
# admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel)
admin.site.register(CarMake)
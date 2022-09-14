from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel

# Register your models here.
class CarModelInline(admin.StackedInline):
    model = CarModel

# CarModelInline class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

    

# CarModelAdmin class
    list_display = ["make",'name',"id", 'type', 'year']
    list_filter = ['year']
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')
# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
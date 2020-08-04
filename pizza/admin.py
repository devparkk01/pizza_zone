from django.contrib import admin
from .models import Size , Pizza, Topping
# Register your models here.

admin.site.register(Pizza)
admin.site.register(Size) 
admin.site.register(Topping)
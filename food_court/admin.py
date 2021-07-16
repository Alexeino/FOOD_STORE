from django.contrib import admin
from .models import Address, City, Food, Sheff
# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    # readonly_fields=("slug",)
    prepopulated_fields = {"slug": ("dish",)}
    list_filter = ("rating","is_popular","sheff")
    list_display = ("id","dish","sheff")
    sortable_by = ("id")

class SheffAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name")

class AddressAdmin(admin.ModelAdmin):
    # list_display=("street","city","postal_code")
    pass


admin.site.register(Food,FoodAdmin)
admin.site.register(Sheff,SheffAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(City)

from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'ContactNumber', 'Address', 'PetName', 'Breed')


admin.site.register(Customer, CustomerAdmin)

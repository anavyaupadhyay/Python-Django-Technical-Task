from django.contrib import admin
from user__app.models import user_model, customer_model

# Register your models here.
@admin.register(user_model)
class user_admin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'mob_no']

@admin.register(customer_model)
class app_admin(admin.ModelAdmin):
    list_display = ['id', 'profile_no']

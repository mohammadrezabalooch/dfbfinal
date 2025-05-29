from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomeUserChageForm, CustomeUserCrationForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomeUserCrationForm
    form = CustomeUserChageForm
    model = CustomUser
    list_display=[
        'username',
        'email',
        'age',
        'is_staff'
    ]
    fieldsets= UserAdmin.fieldsets + ((None,{"fields":("age",)}),)
    add_fieldsets= UserAdmin.add_fieldsets + ((None,{"fields":("age",)}),)

admin.site.register(CustomUser,CustomUserAdmin)
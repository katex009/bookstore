from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'is_superuser', ]
    list_filter = ['is_staff', 'is_active', ]	

admin.site.register(CustomUser, CustomUserAdmin)


    

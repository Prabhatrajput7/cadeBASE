from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUser

class UserAdmin(UserAdmin):
    model = User
    add_form = CustomUser

    fieldsets = (
        (None, {'fields': ('email', 'username','password', )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
            (_('user_info'), {'fields': ('native_name', 'phone_no')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ['email', 'username', 'is_staff', "native_name", "phone_no"]
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', )

admin.site.register(User, UserAdmin)

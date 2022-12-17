from django.contrib import admin
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import User, JD, Application
from .forms import CustomUser

class UserAdmin(UserAdmin):
    model = User
    add_form = CustomUser

    fieldsets = (
        (None, {'fields': ('email', 'username','password', )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_seeker', "is_rec",'is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('dob','last_login', 'date_joined')}),
            (_('user_info'), {'fields': ('mobile','gender')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ['email', 'username', 'is_seeker', "is_rec"]
    search_fields = ('email', 'username')
    ordering = ('email', )

admin.site.register(User, UserAdmin)

admin.site.register(JD)
admin.site.register(Application)




from django.contrib import admin
from .models import Custom
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = Custom
    search_fields = ('email', 'username', 'first_name',)#adding search
    list_filter = ('email', 'username','phone', 'first_name', 'is_active', 'is_staff')#adding filter
    ordering = ('-start_date',) #ording the table
    list_display = ('email', 'username', 'phone','first_name',
                    'is_active', 'is_staff')#displaying the cols
    fieldsets = (
        (None, {'fields': ('email', 'username', 'phone','first_name','password')}),
        ('Permissions', {'fields': ('is_superuser','is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),#adding form
    )
    formfield_overrides = {
        Custom.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},#styling
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','phone' ,'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(Custom, UserAdminConfig)
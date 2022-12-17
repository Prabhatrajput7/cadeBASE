from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email' ,)#adding search
    list_filter = ('email' ,)#adding filter
    list_display = ('email' , 'first_name','is_ambassador')#displaying the cols
    ordering = ('email',)                    
    fieldsets = (
        (None, {'fields': ('email' ,'first_name','last_name','password')}),
        ('Permissions', {'fields': ('is_superuser','is_staff', 'is_active','is_ambassador')}),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', )
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email' ,'first_name', 'password1', 'password2', 'is_superuser','is_active', 'is_staff','is_ambassador')}
         ),
    )


admin.site.register(User, UserAdminConfig)
admin.site.register(Product)
admin.site.register(Link)
admin.site.register(Order)
admin.site.register(OrderItem)
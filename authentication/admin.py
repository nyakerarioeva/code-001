from django.contrib import admin
from authentication.models import MyUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here

class MyUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'profession','date_joined','last_login','is_admin','is_active')
    search_fields = ('username', 'profession')
    readonly_fields = ('date_joined','last_login')
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = ()
    
    add_fieldsets = (
        (None,{
            'classes':('wide'),
            'fields':('email','profession','username','password1','password2'),
        }),
    )
    
    ordering = ('email',)

admin.site.register(MyUser,MyUserAdmin)

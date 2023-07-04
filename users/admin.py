from django.contrib import admin
from .models import CustomUser

from gear.models import Guitar

class GuitarInLine(admin.TabularInline):
    model = Guitar
    extra = 0
    exclude = []

class CustomUserAdmin(admin.ModelAdmin):
    exclude = ['password']
    readonly_fields = ['last_login', 'date_joined', 'average_rating']
    inlines = [GuitarInLine]

    class Meta:
        model = CustomUser

    
admin.site.register(CustomUser, CustomUserAdmin)
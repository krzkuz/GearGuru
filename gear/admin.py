from django.contrib import admin

from .models import (Guitar, BassGuitarProxy, ElectricGuitarProxy, 
    AcousticGuitarProxy, ClassicalGuitarProxy)


class GuitarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model']
    class Meta:
        model = Guitar

    def get_queryset(self, request):
        return Guitar.objects.all()
    
admin.site.register(Guitar, GuitarAdmin)


class BassGuitarProxyAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model']
    class Meta:
        model = BassGuitarProxy

    def get_queryset(self, request):
        return BassGuitarProxy.objects.all()
    
admin.site.register(BassGuitarProxy, BassGuitarProxyAdmin)


class ElectricGuitarProxyAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model']
    class Meta:
        model = ElectricGuitarProxy

    def get_queryset(self, request):
        return ElectricGuitarProxy.objects.all()
    
admin.site.register(ElectricGuitarProxy, ElectricGuitarProxyAdmin)


class AcousticGuitarProxyAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model']
    class Meta:
        model = AcousticGuitarProxy

    def get_queryset(self, request):
        return AcousticGuitarProxy.objects.all()
    
admin.site.register(AcousticGuitarProxy, AcousticGuitarProxyAdmin)


class ClassicalGuitarProxyAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model']
    class Meta:
        model = ClassicalGuitarProxy

    def get_queryset(self, request):
        return ClassicalGuitarProxy.objects.all()
    
admin.site.register(ClassicalGuitarProxy, ClassicalGuitarProxyAdmin)

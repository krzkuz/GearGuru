from django.contrib import admin

from .model_choices import TransactionTypeChoices
from .models import (Guitar, BassGuitarProxy, ElectricGuitarProxy, 
    AcousticGuitarProxy, ClassicalGuitarProxy)
from advertisement.models import Exchange, Rent, Sell, Image


class Inline(admin.ModelAdmin):
    def get_inline_instances(self, request, obj=None):
            inline_instances = super().get_inline_instances(request, obj)
            inline_instances += [ImageInLine(self.model, self.admin_site)]

            if obj and obj.transaction_type == TransactionTypeChoices.EXCHANGE:
                inline_instances += [ExchangeInLine(self.model, self.admin_site)]

            if obj and obj.transaction_type == TransactionTypeChoices.SELL:
                inline_instances += [SellInLine(self.model, self.admin_site)]

            if obj and obj.transaction_type == TransactionTypeChoices.RENT:
                inline_instances += [RentInLine(self.model, self.admin_site)]

            return inline_instances
    

class ImageInLine(admin.TabularInline):
    model = Image
    extra = 0
    # list_display = ['brand', 'model', 'more_info']


class ExchangeInLine(admin.TabularInline):
    model = Exchange
    extra = 0
    list_display = ['brand', 'model', 'more_info']


class RentInLine(admin.TabularInline):
    model = Rent
    extra = 0
    list_display = ['brand', 'model', 'more_info']


class SellInLine(admin.TabularInline):
    model = Sell
    extra = 0
    list_display = ['brand', 'model', 'more_info']


class GuitarAdmin(Inline):
    list_display = ['brand', 'model']
    class Meta:
        model = Guitar

    def get_queryset(self, request):
        return Guitar.objects.all()
    
    def get_inline_instances(self, request, obj=None):
        return super().get_inline_instances(request, obj)
    
admin.site.register(Guitar, GuitarAdmin)


class BassGuitarProxyAdmin(Inline):
    list_display = ['brand', 'model']
    class Meta:
        model = BassGuitarProxy
    
    def get_inline_instances(self, request, obj=None):
        return super().get_inline_instances(request, obj)

    def get_queryset(self, request):
        return BassGuitarProxy.objects.all()
    
admin.site.register(BassGuitarProxy, BassGuitarProxyAdmin)


class ElectricGuitarProxyAdmin(Inline):
    list_display = ['brand', 'model']
    class Meta:
        model = ElectricGuitarProxy

    def get_inline_instances(self, request, obj=None):
        return super().get_inline_instances(request, obj)

    def get_queryset(self, request):
        return ElectricGuitarProxy.objects.all()
    
admin.site.register(ElectricGuitarProxy, ElectricGuitarProxyAdmin)


class AcousticGuitarProxyAdmin(Inline):
    list_display = ['brand', 'model']
    class Meta:
        model = AcousticGuitarProxy
    
    def get_inline_instances(self, request, obj=None):
        return super().get_inline_instances(request, obj)

    def get_queryset(self, request):
        return AcousticGuitarProxy.objects.all()
    
admin.site.register(AcousticGuitarProxy, AcousticGuitarProxyAdmin)


class ClassicalGuitarProxyAdmin(Inline):
    list_display = ['brand', 'model']
    class Meta:
        model = ClassicalGuitarProxy
    
    def get_inline_instances(self, request, obj=None):
        return super().get_inline_instances(request, obj)

    def get_queryset(self, request):
        return ClassicalGuitarProxy.objects.all()
    
admin.site.register(ClassicalGuitarProxy, ClassicalGuitarProxyAdmin)

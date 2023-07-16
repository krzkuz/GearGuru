from django.contrib import admin

from .models import Rent, Sell, Exchange, Image


class RentAdmin(admin.ModelAdmin):
    class Meta:
        model = Rent

    def get_queryset(self, request):
        return Rent.objects.all()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title'].required = False
        form.base_fields['price'].required = False
        form.base_fields['renting_time'].required = False
        form.base_fields['more_info'].required = False

        return form
    
admin.site.register(Rent, RentAdmin)


class SellAdmin(admin.ModelAdmin):
    class Meta:
        model = Sell
    
    def get_queryset(self, request):
        return Sell.objects.all()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title'].required = False
        form.base_fields['price'].required = False
        form.base_fields['more_info'].required = False
        return form

admin.site.register(Sell, SellAdmin)


class ExchangeAdmin(admin.ModelAdmin):
    # list_display = ['brand', 'model', 'related_gear']
    
    class Meta:
        model = Exchange

    def get_queryset(self, request):
        return Exchange.objects.all()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['brand'].required = False
        form.base_fields['model'].required = False
        form.base_fields['more_info'].required = False
        return form
    
admin.site.register(Exchange, ExchangeAdmin)

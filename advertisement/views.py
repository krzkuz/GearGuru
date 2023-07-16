from django.shortcuts import render
from django.views.generic import ListView, DetailView

from gear.models import (Guitar, ElectricGuitarProxy, BassGuitarProxy, 
    AcousticGuitarProxy, ClassicalGuitarProxy)
from advertisement.models import Rent, Sell, Exchange
from gear.model_choices import TransactionTypeChoices

class HomePageView(ListView):
    model = Guitar
    template_name = 'advertisement/guitars_list.html'
    context_object_name = 'guitars'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     for obj in queryset:
    #         obj. 
    #     return queryset

class AdvertisementView(DetailView):
    model = Guitar
    template_name = 'advertisement/guitar.html'
    context_object_name = 'guitar'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        transaction_type = self.object.transaction_type
        if transaction_type == TransactionTypeChoices.RENT:
            rent = Rent.objects.get(related_gear=self.object)
            context['rent'] = rent
        elif transaction_type == TransactionTypeChoices.SELL:
            sell = Sell.objects.get(related_gear=self.object)
            context['sell'] = sell
        else:
            exchange = Exchange.objects.get(related_gear=self.object)
            context['exchange'] = exchange
        return context
    

class TransactionMixin(ListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        transaction_type = self.request.GET.get('transaction')
        if transaction_type:
            queryset = queryset.filter(transaction_type=transaction_type)
        return queryset
    

class ElectricGuitarsView(TransactionMixin,ListView):
    model = ElectricGuitarProxy
    template_name = 'advertisement/guitars_list.html'
    context_object_name = 'guitars'


class BassGuitarsView(TransactionMixin, ListView):
    model = BassGuitarProxy
    template_name = 'advertisement/guitars_list.html'
    context_object_name = 'guitars'


class AcousticGuitarsView(TransactionMixin, ListView):
    model = AcousticGuitarProxy
    template_name = 'advertisement/guitars_list.html'
    context_object_name = 'guitars'


class ClassicalGuitarsView(TransactionMixin, ListView):
    model = ClassicalGuitarProxy
    template_name = 'advertisement/guitars_list.html'
    context_object_name = 'guitars'

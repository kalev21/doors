from cloudipsp import Api, Checkout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import FeedBackModel, ProductsCardModel, ContactModel, DeliverModel
from .forms import FeedBackForm
from django.views.generic import CreateView, ListView


def index(request):
    return render(request, 'shop/index.html')


class ContactView(ListView):    # Вьюха контакты
    model = ContactModel
    template_name = 'shop/contact.html'
    context_object_name = 'contacts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        return context


class FeedBackView(CreateView, ListView):  # Вьюха отзывы
    model = FeedBackModel
    form_class = FeedBackForm
    template_name = 'shop/feedback.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('shop:feedback')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # Важная строка кода (иначе все потеряется)
        return context


class CatalogView(ListView):    # Вьюха каталога товаров
    model = ProductsCardModel
    template_name = 'shop/catalog.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return ProductsCardModel.objects.order_by('-id')


def buy(request, id):   # Покупка товара
    products = ProductsCardModel.objects.get(id=id)

    api = Api(merchant_id=1396424, secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "RUB",
        "amount": str(products.price) + '00'
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)


class DeliveryView(ListView):
    model = DeliverModel
    template_name = 'shop/delivery.html'
    context_object_name = 'delivers'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DeliveryView, self).get_context_data(**kwargs)
        return context


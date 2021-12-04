from django.urls import path

from . import views
from .views import FeedBackView, CatalogView, ContactView, DeliveryView

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact', ContactView.as_view(), name='contact'),
    path('feedback', FeedBackView.as_view(), name='feedback'),
    path('catalog', CatalogView.as_view(), name='catalog'),
    path('buy/<int:id>', views.buy, name='buy'),
    path('delivery', DeliveryView.as_view(), name='delivery')
]


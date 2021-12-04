from django.contrib import admin
from .models import FeedBackModel, ProductsCardModel, Category, ContactModel, DeliverModel


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_filter = ('name', )
    prepopulated_fields = {'slug': ('name', )}  # автоматическая транслитерация


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'image', 'description', 'price', 'category')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('name', 'price', 'category')
    prepopulated_fields = {'slug': ('name',)}  # автоматическая транслитерация


class FeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'publish_date')
    list_display_links = ('id', 'author')
    search_fields = ('author', 'publish_date')
    list_filter = ('author', 'publish_date')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'phone', 'hours', 'site', 'email')
    list_display_links = ('id', 'site')
    search_fields = ('phone', 'site', 'email')


admin.site.register(FeedBackModel, FeedAdmin)
admin.site.register(ProductsCardModel, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ContactModel, ContactAdmin)
admin.site.register(DeliverModel)


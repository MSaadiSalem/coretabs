from django.contrib import admin

from .models import Product, Category


# Admin Site Customization
admin.site.site_header = "Coretabe Online Shop Administration"
admin.site.site_title = "Coretabs Online Shop Administration"
admin.site.index_title = ""  # Change "Site Administration" to an empty text.


# ModelAdmin Customization
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"  # Add timeline to Products
    search_fields = ['name']
    list_display = ('name', 'price', 'stock', 'category',)
    list_filter = ('created_at', 'category')
    actions = ['make_price_zero', 'discount_20']

    # Actions
    def make_price_zero(modeladmin, request, queryset):
        queryset.update(price=0)
    make_price_zero.short_description = "Make selected products free"

    def discount_20(modeladmin, request, queryset):
        for product in queryset:
            new_price = product.price * 80 / 100
            queryset.update(price=new_price)

    discount_20.short_description = "Discount 20%% for selected products"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    search_fields = ['name']
    list_display = ('name', 'description')

from django.contrib import admin
from .models import Product_type, Goods, Prop_laptop, Prop_mobile, Counterparties, Prices


# Register your models here.


class Product_typeAdmin(admin.ModelAdmin):
    list_display = ('id', 'typ')
    list_display_links = ('typ',)
    search_fields = ('typ',)


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'good_name', 'image', 'product_type_id')
    list_display_links = ('good_name', 'product_type_id')
    search_fields = ('good_name', 'product_type_id')
    #
    # list_display = ('id', 'good_name', 'typ_name')
    # list_display_links = ('good_name', 'typ_name')
    # search_fields = ('good_name', 'typ_name')



class Prop_laptopAdmin(admin.ModelAdmin):
    list_display = ('id', 'screen', 'ram', 'cpu', 'video_card', 'goods_id')
    list_display_links = ('goods_id',)
    search_fields = ('goods_id',)


class Prop_mobileAdmin(admin.ModelAdmin):
    list_display = ('id', 'screen', 'cpu', 'battery', 'goods_id')
    list_display_links = ('goods_id',)
    search_fields = ('goods_id',)


class CounterpartiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)


class PricesAdmin(admin.ModelAdmin):
    list_display = ('id', 'price_buy', 'price_sell', 'criteria', 'goods_id', 'counterparties_id')
    list_display_links = ('price_sell', 'goods_id', 'counterparties_id')
    search_fields = ('goods_id',)


admin.site.register(Product_type, Product_typeAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Prop_laptop, Prop_laptopAdmin)
admin.site.register(Prop_mobile, Prop_mobileAdmin)
admin.site.register(Counterparties, CounterpartiesAdmin)
admin.site.register(Prices, PricesAdmin)

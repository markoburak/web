from rest_framework import serializers
from .models import Product_type, Goods, Prop_mobile, Prop_laptop, Counterparties, Prices


class product_typeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product_type
        fields = '__all__'


class counterpartiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Counterparties
        fields = '__all__'


class goodsSerializers(serializers.ModelSerializer):
    typ_names = product_typeSerializers(read_only=True, source='product_type_id')
    product_type_id = serializers.SlugRelatedField(write_only=True, queryset=Product_type.objects.all(),
                                                   slug_field='typ')

    class Meta:
        model = Goods
        fields = '__all__'


class prop_laptopSerializers(serializers.ModelSerializer):
    good_name2 = goodsSerializers(read_only=True, source='goods_id')
    goods_id = serializers.SlugRelatedField(write_only=True, queryset=Goods.objects.all(), slug_field='good_name')

    class Meta:
        model = Prop_laptop
        fields = '__all__'


class prop_mobileSerializers(serializers.ModelSerializer):
    good_name2 = goodsSerializers(read_only=True, source='goods_id')
    goods_id = serializers.SlugRelatedField(write_only=True, queryset=Goods.objects.all(), slug_field='good_name')

    class Meta:
        model = Prop_mobile
        fields = '__all__'


class pricesSerializers(serializers.ModelSerializer):
    good_name2 = goodsSerializers(read_only=True, source='goods_id')
    goods_id = serializers.SlugRelatedField(write_only=True, queryset=Goods.objects.all(), slug_field='good_name')
    counterparties_name = counterpartiesSerializers(read_only=True, source='counterparties_id')
    counterparties_id = serializers.SlugRelatedField(write_only=True, queryset=Counterparties.objects.all(),
                                                     slug_field='name')

    class Meta:
        model = Prices
        fields = '__all__'

from django.db import models

from django.core.validators import RegexValidator


class Product_type(models.Model):
    typ = models.CharField(max_length=45, db_index=True, verbose_name='Тип товару')

    def __str__(self):
        return self.typ

    class Meta:
        verbose_name_plural = 'Типи'
        verbose_name = 'Тип'
        ordering = ['typ']


class Goods(models.Model):
    good_name = models.CharField(max_length=45, db_index=True, verbose_name="Імя товару")
    image = models.CharField(max_length=255, verbose_name='шлях до малюнку', null=True)
    product_type_id = models.ForeignKey(Product_type, on_delete=models.CASCADE, verbose_name='тип')
    # typ_name = models.ForeignKey(Product_type, on_delete=models.CASCADE, verbose_name='тип')

    def __str__(self):
        return self.good_name

    class Meta:
        verbose_name_plural = 'Товари'
        verbose_name = 'Товар'
        ordering = ['id']


class Prop_laptop(models.Model):
    screen = models.CharField(max_length=45, null=True, verbose_name='Дисплей')
    ram = models.CharField(max_length=45, null=True, verbose_name="Оперативна пам'ять")
    cpu = models.CharField(max_length=45, null=True, verbose_name="Процесор")
    video_card = models.CharField(max_length=45, null=True, verbose_name="Відеокарта")
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='товар')

    def __str__(self):
        return self.screen

    class Meta:
        verbose_name_plural = "Властивості ноутбуків"
        verbose_name = 'Властивість ноутбука'
        ordering = ['id']


class Prop_mobile(models.Model):
    screen = models.CharField(max_length=45, null=True, verbose_name='Дисплей')
    cpu = models.CharField(max_length=45, null=True, verbose_name="Процесор")
    battery = models.CharField(max_length=45, null=True, verbose_name="Батарея")
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='товар')

    def __str__(self):
        return self.screen

    class Meta:
        verbose_name_plural = "Властивості телефонів"
        verbose_name = 'Властивість телефону'
        ordering = ['id']


class Counterparties(models.Model):
    name = models.CharField(max_length=60, db_index=True, verbose_name="ім'я контрагента")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'контрагенти'
        verbose_name = 'контрагент'
        ordering = ['id']


class Prices(models.Model):
    price_buy = models.FloatField(db_index=True, verbose_name="закупна ціна")
    price_sell = models.FloatField(db_index=True, verbose_name="ціна продажу")
    criteria = models.BooleanField(verbose_name='критерія про наявність')
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='товар')
    counterparties_id = models.ForeignKey(Counterparties, on_delete=models.CASCADE, verbose_name='контрагент')

    def __float__(self):
        return self.price_sell

    class Meta:
        verbose_name_plural = 'ціни'
        verbose_name = 'ціна'
        ordering = ['id']

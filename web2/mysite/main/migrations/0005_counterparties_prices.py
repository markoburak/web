# Generated by Django 3.0.2 on 2020-04-08 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200408_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='counterparties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=60, verbose_name="ім'я контрагента")),
            ],
            options={
                'verbose_name': 'контрагент',
                'verbose_name_plural': 'контрагенти',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_buy', models.FloatField(db_index=True, verbose_name='закупна ціна')),
                ('price_sell', models.FloatField(db_index=True, verbose_name='ціна продажу')),
                ('criteria', models.BooleanField(verbose_name='критерія про наявність')),
                ('counterparties_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.counterparties', verbose_name='контрагент')),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.goods', verbose_name='товар')),
            ],
            options={
                'verbose_name': 'ціна',
                'verbose_name_plural': 'ціни',
                'ordering': ['id'],
            },
        ),
    ]

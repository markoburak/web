# Generated by Django 3.0.2 on 2020-04-08 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_prop_laptop'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prop_laptop',
            options={'ordering': ['id'], 'verbose_name': 'Властивість ноутбука', 'verbose_name_plural': 'Властивості ноутбуків'},
        ),
    ]

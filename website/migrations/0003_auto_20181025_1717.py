# Generated by Django 2.1.1 on 2018-10-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_cart_quan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quan',
            field=models.IntegerField(default=1),
        ),
    ]

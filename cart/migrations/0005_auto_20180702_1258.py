# Generated by Django 2.0.2 on 2018-07-02 07:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20180702_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete='cascade', related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 3.0.8 on 2020-08-04 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_auto_20200804_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='topping1',
            field=models.CharField(max_length=100),
        ),
    ]

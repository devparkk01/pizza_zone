# Generated by Django 3.0.8 on 2020-08-04 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_pizza_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='pizza',
            name='topping1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Topping'),
        ),
    ]

# Generated by Django 3.2.16 on 2022-12-12 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='pizza_name',
            new_name='name',
        ),
        migrations.DeleteModel(
            name='Toppings',
        ),
        migrations.AddField(
            model_name='topping',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.pizza'),
        ),
    ]

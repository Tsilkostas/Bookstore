# Generated by Django 4.0.4 on 2022-04-26 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_name', models.CharField(help_text='Required', max_length=255, verbose_name='delivery_name')),
                ('delivery_price', models.DecimalField(decimal_places=2, default=0.0, error_messages={'name': {'max_length': 'The price must be between 0 and 999.99.'}}, help_text='Maximum 999.99', max_digits=5, verbose_name='delivery price')),
                ('delivery_method', models.CharField(choices=[('DD', 'Digital Delivery')], default=False, help_text='Required', max_length=255, verbose_name='delivery_method')),
                ('order', models.IntegerField(default=0, help_text='Required', verbose_name='list order')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Delivery Option',
                'verbose_name_plural': 'Delivery Options',
            },
        ),
        migrations.CreateModel(
            name='PaymentSelections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=255, verbose_name='name')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Payment Selection',
                'verbose_name_plural': 'Payment Selections',
            },
        ),
    ]

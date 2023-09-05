# Generated by Django 4.2.4 on 2023-08-30 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_twieet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cretificate_name', models.CharField(max_length=50)),
                ('cretificate_price', models.DecimalField(decimal_places=4, max_digits=10, max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingDirection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=100)),
                ('jon_size', models.DecimalField(decimal_places=4, max_digits=10, max_length=8)),
                ('jon_count', models.BigIntegerField(null=True)),
                ('value_ofTonToLiter', models.BigIntegerField(null=True)),
                ('joi_price', models.DecimalField(decimal_places=4, max_digits=10, max_length=8)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sticker_company', models.CharField(max_length=100)),
                ('sticker_size', models.DecimalField(decimal_places=3, max_digits=10, max_length=6)),
                ('sticker_price', models.DecimalField(decimal_places=3, max_digits=10, max_length=6)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('jerecan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('trip_Price', models.DecimalField(decimal_places=5, max_digits=10, max_length=10)),
                ('trip_date', models.CharField(max_length=100)),
                ('trip_Time', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('certification', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.certificate')),
                ('direction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.shippingdirection')),
            ],
        ),
        migrations.CreateModel(
            name='OilSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oil_company', models.CharField(max_length=100)),
                ('oil_name', models.CharField(max_length=50)),
                ('oil_quantity', models.DecimalField(decimal_places=5, max_digits=10, max_length=10)),
                ('oil_price', models.DecimalField(decimal_places=5, max_digits=10, max_length=10)),
                ('oil_month_selling', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('jerecan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Cartoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartoon_company', models.CharField(max_length=100)),
                ('cartoon_size', models.DecimalField(decimal_places=4, max_digits=10, max_length=8)),
                ('cartoon_price', models.DecimalField(decimal_places=4, max_digits=10, max_length=8)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('jearecane', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.supplier')),
            ],
        ),
    ]

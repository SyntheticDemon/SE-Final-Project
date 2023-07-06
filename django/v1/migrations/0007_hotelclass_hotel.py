# Generated by Django 4.2.2 on 2023-07-05 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0006_alter_package_package_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_class', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('capacity', models.DecimalField(decimal_places=0, max_digits=12)),
                ('cost', models.DecimalField(decimal_places=0, max_digits=12)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.city')),
                ('hotel_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.hotelclass')),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-05 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0007_hotelclass_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatmentrequest',
            name='reserved_hotel_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='v1.hotel'),
        ),
    ]
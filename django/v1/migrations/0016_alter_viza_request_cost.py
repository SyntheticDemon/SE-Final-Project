# Generated by Django 4.2.2 on 2023-07-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0015_alter_vizadocument_related_visa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viza',
            name='request_cost',
            field=models.DecimalField(decimal_places=0, default=50000, max_digits=12),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-08 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_equipment_options_alter_loan_options_and_more'),
        ('customadmin', '0003_profile_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='vehicle',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.vehicle'),
        ),
    ]

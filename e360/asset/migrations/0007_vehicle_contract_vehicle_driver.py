# Generated by Django 4.2.6 on 2023-11-17 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_alter_equippayoff_options_and_more'),
        ('customadmin', '0005_remove_profile_vehicle'),
        ('asset', '0006_equipment_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.loan'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='driver',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customadmin.profile'),
        ),
    ]

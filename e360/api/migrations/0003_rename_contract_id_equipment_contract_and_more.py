# Generated by Django 4.2.6 on 2023-10-31 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_equipment_contract_id_vehicle_contract_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='contract_id',
            new_name='contract',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='contract_id',
            new_name='contract',
        ),
    ]

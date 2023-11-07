# Generated by Django 4.2.6 on 2023-11-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_loan_link_to_contract'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipment',
            options={'ordering': ['equipment_id']},
        ),
        migrations.AlterModelOptions(
            name='loan',
            options={'ordering': ['lender', 'contract_number']},
        ),
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ['equipment_id']},
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Satisfied', 'Satisfied')], default='Active', max_length=20, null=True),
        ),
    ]

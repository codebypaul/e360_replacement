# Generated by Django 4.2.6 on 2023-11-01 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_loan_financed_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='lender',
            field=models.CharField(max_length=40),
        ),
    ]

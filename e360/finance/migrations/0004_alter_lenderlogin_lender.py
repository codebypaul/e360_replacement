# Generated by Django 4.2.6 on 2023-11-15 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_alter_equippayoff_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lenderlogin',
            name='lender',
            field=models.CharField(blank=True, null=True),
        ),
    ]
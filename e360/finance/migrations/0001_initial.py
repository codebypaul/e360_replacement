# Generated by Django 4.2.6 on 2023-11-10 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0017_alter_vehicle_vin'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehiclePayoff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payoff_amount', models.FloatField(blank=True, null=True)),
                ('as_of_date', models.DateField(blank=True, null=True)),
                ('fair_market_value', models.IntegerField(blank=True, null=True)),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.loan')),
                ('vehicle', models.OneToOneField(db_column='vehicle_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='EquipPayoff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payoff_amount', models.FloatField(blank=True, null=True)),
                ('as_of_date', models.DateField(blank=True, null=True)),
                ('fair_market_value', models.IntegerField(blank=True, null=True)),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.loan')),
                ('equipment', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.equipment')),
            ],
        ),
    ]

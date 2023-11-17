# Generated by Django 4.2.6 on 2023-11-16 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_alter_location_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], null=True)),
                ('serial_number', models.CharField(max_length=30)),
                ('year', models.PositiveSmallIntegerField(null=True)),
                ('description', models.CharField(max_length=100)),
                ('ownership', models.CharField(choices=[('Financed', 'Financed'), ('Rental', 'Rental'), ('InterCo', 'Inter Company Rental'), ('Leased', 'Leased'), ('Owned', 'Owned'), ('Sold', 'Sold'), ('Unknown', 'Unknown')], max_length=20)),
                ('hours', models.IntegerField()),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['equipment_id'],
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('equipment_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], null=True)),
                ('vin', models.CharField(max_length=17, unique=True)),
                ('year', models.PositiveSmallIntegerField(null=True)),
                ('description', models.CharField(max_length=100)),
                ('ownership', models.CharField(choices=[('Financed', 'Financed'), ('Rental', 'Rental'), ('InterCo', 'Inter Company Rental'), ('Leased', 'Leased'), ('Owned', 'Owned w/ Title'), ('Newly Owned', 'Owned w/o Title'), ('Sold', 'Sold'), ('Unknown', 'Unknown')], max_length=20)),
                ('mileage', models.IntegerField()),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['equipment_id'],
            },
        ),
    ]

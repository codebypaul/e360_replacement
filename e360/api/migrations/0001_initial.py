# Generated by Django 4.2.6 on 2023-10-31 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('serial_number', models.CharField(max_length=20)),
                ('year', models.PositiveSmallIntegerField(null=True)),
                ('description', models.CharField(max_length=100)),
                ('ownership', models.CharField(choices=[('Financed', 'Financed'), ('Rental', 'Rental'), ('InterCo', 'Inter Company Rental'), ('Leased', 'Leased'), ('Owned', 'Owned w/ Title'), ('Unknown', 'Unknown')], max_length=15)),
                ('hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('contract_id', models.AutoField(primary_key=True, serialize=False)),
                ('lender', models.CharField(max_length=30)),
                ('owned_company', models.CharField(max_length=25)),
                ('contract_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('equipment_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('vin', models.CharField(max_length=17)),
                ('year', models.PositiveSmallIntegerField(null=True)),
                ('description', models.CharField(max_length=100)),
                ('ownership', models.CharField(choices=[('Financed', 'Financed'), ('Rental', 'Rental'), ('InterCo', 'Inter Company Rental'), ('Leased', 'Leased'), ('Owned', 'Owned w/ Title'), ('Unknown', 'Unknown')], max_length=15)),
                ('mileage', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 3.0.7 on 2020-09-25 12:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=23)),
                ('town', models.CharField(max_length=34)),
                ('postcode', models.CharField(default='43701', max_length=5, verbose_name='zip code')),
                ('state', models.CharField(max_length=34)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True)),
                ('pre_symbol', models.CharField(blank=True, max_length=1)),
                ('post_symbol', models.CharField(blank=True, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Customer_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('TS', 'Transgender')], max_length=50)),
                ('Customer_profilepic', models.FileField(upload_to='')),
                ('Customer_Email', models.EmailField(max_length=111)),
                ('Customer_created_at', models.DateTimeField(auto_now_add=True)),
                ('Customer_PhoneNo1', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Customer_Street', models.CharField(default='', max_length=250)),
                ('Customer_Landmark', models.CharField(default='', max_length=100)),
                ('Customer_Zipcode', models.IntegerField(default='')),
                ('Customer_State', models.CharField(default='', max_length=100)),
                ('Customer_Country', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='location1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=23)),
                ('city', models.CharField(max_length=23)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('amount', models.IntegerField(default=0)),
                ('phone', models.CharField(default='', max_length=111)),
                ('coursename', models.CharField(max_length=5000)),
                ('prices', models.CharField(max_length=500)),
                ('qty', models.CharField(max_length=400)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 25, 18, 3, 13, 630139))),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('address', models.CharField(max_length=34)),
                ('invoice_id', models.CharField(blank=True, editable=False, max_length=6, null=True, unique=True)),
                ('invoice_date', models.DateField(default=datetime.date.today)),
                ('invoiced', models.BooleanField(default=False)),
                ('draft', models.BooleanField(default=False)),
                ('paid_date', models.DateField(blank=True, null=True)),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Currency')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm.customer')),
            ],
            options={
                'ordering': ('-invoice_date', 'id'),
            },
        ),
    ]
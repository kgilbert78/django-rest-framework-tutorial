# Generated by Django 4.2 on 2023-04-23 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_app', '0002_owner_car_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=20)),
                ('warranty_num_years', models.PositiveIntegerField(default=1)),
                ('finance_plan', models.CharField(default='unavailable', max_length=20)),
            ],
        ),
    ]

# Generated by Django 4.2 on 2023-05-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('car_brand', models.CharField(max_length=50)),
                ('round_finishing_time', models.IntegerField(default=0)),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treevkusa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('weight', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]

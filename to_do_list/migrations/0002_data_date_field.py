# Generated by Django 3.1.2 on 2021-02-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='date_field',
            field=models.DateField(auto_now=True),
        ),
    ]

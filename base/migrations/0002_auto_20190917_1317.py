# Generated by Django 2.2.2 on 2019-09-17 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='logo',
            field=models.FileField(upload_to=''),
        ),
    ]

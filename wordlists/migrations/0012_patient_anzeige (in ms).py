# Generated by Django 3.2.5 on 2023-06-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordlists', '0011_auto_20230408_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Anzeige (in ms)',
            field=models.IntegerField(default=1000),
        ),
    ]
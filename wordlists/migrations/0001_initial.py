# Generated by Django 3.2.5 on 2022-12-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wordlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.TextField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]

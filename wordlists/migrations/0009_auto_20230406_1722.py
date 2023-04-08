# Generated by Django 3.2.5 on 2023-04-06 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wordlists', '0008_auto_20230405_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wordlist',
            name='duration',
        ),
        migrations.AlterField(
            model_name='test',
            name='duration',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='wordlist',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vorname', models.CharField(max_length=60)),
                ('Nachname', models.CharField(max_length=60)),
                ('Profilbild', models.ImageField(upload_to='')),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

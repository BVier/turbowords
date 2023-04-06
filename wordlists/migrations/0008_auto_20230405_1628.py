# Generated by Django 3.2.5 on 2023-04-05 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wordlists', '0007_rename_usertests_userwordlists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwordlists',
            name='wordlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filter', to='wordlists.wordlist'),
        ),
        migrations.AlterField(
            model_name='wordlist',
            name='duration',
            field=models.IntegerField(default=1000),
        ),
    ]
# Generated by Django 3.2.5 on 2023-01-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordlists', '0004_test_shuffled_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='correct_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='word_count',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-09 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('language_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='languagepoamodel',
            options={'ordering': ['language'], 'verbose_name_plural': 'ПОЯ тексты'},
        ),
    ]
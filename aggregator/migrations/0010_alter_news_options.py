# Generated by Django 3.2.7 on 2021-09-30 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0009_alter_news_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-published']},
        ),
    ]

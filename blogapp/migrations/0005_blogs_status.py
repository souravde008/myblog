# Generated by Django 2.2a1 on 2021-06-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20210618_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 2.2a1 on 2021-06-23 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_blogs_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 2.2a1 on 2021-06-18 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20210618_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blogapp.Users'),
        ),
    ]

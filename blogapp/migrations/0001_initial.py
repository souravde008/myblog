# Generated by Django 2.2a1 on 2021-06-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_mail', models.EmailField(max_length=70)),
                ('user_phone', models.CharField(max_length=100)),
            ],
        ),
    ]
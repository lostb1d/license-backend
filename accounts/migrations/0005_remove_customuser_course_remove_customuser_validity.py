# Generated by Django 4.2.13 on 2024-05-24 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_validity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='course',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='validity',
        ),
    ]
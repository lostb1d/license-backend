# Generated by Django 4.2.13 on 2024-05-24 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_customuser_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='validity',
            field=models.DateField(blank=True, null=True),
        ),
    ]
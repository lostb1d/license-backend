# Generated by Django 4.2.13 on 2024-05-23 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geomatics', '0004_questions_publish_questions_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='chapter',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='geomatics.chapter'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.13 on 2024-05-24 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geomatics', '0007_remove_cartographyandgeovisualization_correctopt_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='questions',
            new_name='geomaticsQuestions',
        ),
    ]

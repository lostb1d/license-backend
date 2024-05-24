# Generated by Django 4.2.13 on 2024-05-23 18:01

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapterCode', models.CharField(max_length=30)),
                ('chapterName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='correctOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correctOpt', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='weightage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', django_quill.fields.QuillField()),
                ('option1', django_quill.fields.QuillField()),
                ('option2', django_quill.fields.QuillField()),
                ('option3', django_quill.fields.QuillField()),
                ('option4', django_quill.fields.QuillField()),
                ('explanation', django_quill.fields.QuillField()),
                ('publish', models.BooleanField(default=False)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civil.chapter')),
                ('correctOpt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civil.correctoption')),
                ('weight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civil.weightage')),
            ],
        ),
    ]

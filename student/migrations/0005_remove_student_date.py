# Generated by Django 3.0.5 on 2022-09-01 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date',
        ),
    ]
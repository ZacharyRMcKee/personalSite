# Generated by Django 2.0.1 on 2018-01-27 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_resume_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='name',
        ),
    ]

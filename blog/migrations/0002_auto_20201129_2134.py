# Generated by Django 3.1.2 on 2020-11-29 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blogpost',
            new_name='blog',
        ),
    ]

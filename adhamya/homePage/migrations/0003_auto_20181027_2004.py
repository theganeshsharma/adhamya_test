# Generated by Django 2.1.2 on 2018-10-27 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0002_auto_20181027_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='Feedback',
            new_name='Comment',
        ),
    ]
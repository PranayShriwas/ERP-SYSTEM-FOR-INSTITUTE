# Generated by Django 4.1.5 on 2023-05-15 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0003_addstudent"),
    ]

    operations = [
        migrations.RenameField(
            model_name="addstudent", old_name="smonile", new_name="smobile",
        ),
    ]

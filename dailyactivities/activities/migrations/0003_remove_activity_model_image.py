# Generated by Django 5.0.6 on 2024-08-12 11:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("activities", "0002_rename_photo_activity_model_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="activity_model",
            name="image",
        ),
    ]

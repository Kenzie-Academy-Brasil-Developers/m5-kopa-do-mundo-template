# Generated by Django 4.1.7 on 2023-04-02 19:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="team",
            old_name="top_soccer",
            new_name="top_scorer",
        ),
    ]
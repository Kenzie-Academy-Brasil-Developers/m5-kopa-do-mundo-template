# Generated by Django 4.2.1 on 2023-06-03 22:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="fifa_code",
            field=models.CharField(max_length=3, unique=True),
        ),
    ]

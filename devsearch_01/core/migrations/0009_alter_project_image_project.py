# Generated by Django 4.1.9 on 2023-05-29 19:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_image_project_tool"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image_project",
            field=models.ManyToManyField(blank=True, to="core.image"),
        ),
    ]
# Generated by Django 4.2.17 on 2024-12-29 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_alter_photoslider_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="aboutus",
            options={"verbose_name": "AboutUs", "verbose_name_plural": "AboutUs"},
        ),
        migrations.AlterModelOptions(
            name="photoslider",
            options={
                "verbose_name": "PhotoSlider",
                "verbose_name_plural": "PhotoSliders",
            },
        ),
    ]

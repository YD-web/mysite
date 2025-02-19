# Generated by Django 5.1.5 on 2025-02-05 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_blogpage_feed_image_blogpage_private_field_and_more"),
        ("wagtailimages", "0027_image_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="date",
            field=models.DateTimeField(verbose_name="Post date"),
        ),
        migrations.AlterField(
            model_name="blogpage",
            name="feed_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="wagtailimages.image",
            ),
        ),
        migrations.AlterField(
            model_name="blogpage",
            name="published_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 5.1.5 on 2025-01-17 07:49

import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_remove_blogpage_authors_remove_blogpage_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpage",
            name="authors",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True, to="blog.author"
            ),
        ),
    ]

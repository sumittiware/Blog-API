# Generated by Django 4.0.2 on 2022-02-27 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='name',
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-12 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='published_date',
            new_name='publication_date',
        ),
    ]
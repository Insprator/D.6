# Generated by Django 4.2.1 on 2023-06-06 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_category_subscribers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='postCategory',
            new_name='category',
        ),
    ]
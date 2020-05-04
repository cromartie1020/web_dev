# Generated by Django 2.2 on 2020-05-04 18:22

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_auto_20200503_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='A label for URL config.', max_length=31, populate_from=['name']),
        ),
    ]

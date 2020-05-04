# Generated by Django 2.2 on 2020-05-03 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_startup_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newslink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(max_length=63)),
                ('pub_date', models.DateField(verbose_name='Date Published')),
                ('link', models.URLField(max_length=255)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Startup')),
            ],
        ),
    ]

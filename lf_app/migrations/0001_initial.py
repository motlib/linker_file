# Generated by Django 3.0.5 on 2020-06-19 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(default='', max_length=1024)),
                ('title', models.CharField(default='', max_length=1024)),
                ('notes', models.TextField(default='')),
            ],
        ),
    ]

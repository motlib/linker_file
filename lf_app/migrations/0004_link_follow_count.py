# Generated by Django 3.0.5 on 2020-06-19 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lf_app', '0003_link_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='follow_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

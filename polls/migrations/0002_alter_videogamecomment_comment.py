# Generated by Django 5.1.6 on 2025-03-31 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogamecomment',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

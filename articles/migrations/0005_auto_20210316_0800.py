# Generated by Django 3.1.7 on 2021-03-16 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210316_0736'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set(),
        ),
    ]

# Generated by Django 3.0.2 on 2020-05-08 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Examportalquiz1', '0014_auto_20200509_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='test3',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

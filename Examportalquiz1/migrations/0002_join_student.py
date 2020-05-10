# Generated by Django 3.0.2 on 2020-05-04 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Examportalquiz1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='join_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classrooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Examportalquiz1.Create_Classroom')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
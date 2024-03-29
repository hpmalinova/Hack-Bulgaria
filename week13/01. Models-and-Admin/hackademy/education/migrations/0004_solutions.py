# Generated by Django 3.0.6 on 2020-05-27 14:04

from django.db import migrations, models
import django.db.models.deletion
import education.validator


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('url', models.URLField(max_length=500, validators=[education.validator.validate_url])),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Task')),
            ],
        ),
    ]

# Generated by Django 5.2 on 2025-04-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal_app', '0003_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary_range',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]

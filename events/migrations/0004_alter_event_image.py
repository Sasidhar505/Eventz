# Generated by Django 3.2.6 on 2021-09-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
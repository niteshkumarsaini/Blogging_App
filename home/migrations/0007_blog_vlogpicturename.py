# Generated by Django 4.2 on 2023-05-05 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='vlogpicturename',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
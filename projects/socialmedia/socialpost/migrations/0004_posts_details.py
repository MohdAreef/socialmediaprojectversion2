# Generated by Django 5.0.2 on 2024-02-20 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialpost', '0003_alter_posts_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='details',
            field=models.TextField(null=True),
        ),
    ]

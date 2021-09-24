# Generated by Django 3.2.5 on 2021-09-24 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_auto_20210924_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='site_last_http_response',
            field=models.IntegerField(default=404),
        ),
        migrations.AlterField(
            model_name='website',
            name='slack_account_url',
            field=models.URLField(default='https://www.rheeder.slack.com'),
        ),
    ]
# Generated by Django 2.1.3 on 2018-11-18 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='test_field',
            field=models.CharField(default='test', max_length=200),
        ),
    ]

# Generated by Django 2.1.3 on 2018-12-17 16:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(error_messages={'required': 'You have to fill this field', 'unique': 'The post with this title already exists, pick another'}, help_text='Must be unique value', max_length=250, unique=True)),
                ('slug', models.CharField(blank=True, max_length=250, null=True)),
                ('featured', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('active', 'Active')], default=('published', 'Published'), max_length=10)),
                ('body', models.TextField(blank=True)),
                ('author_email', models.CharField(blank=True, editable=False, max_length=240, null=True)),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Author')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]

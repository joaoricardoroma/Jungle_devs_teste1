# Generated by Django 4.0.4 on 2022-05-09 18:21

import app.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=app.models.upload_image_author, verbose_name='picture')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=500)),
                ('first_paragraph', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=10000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_author', to='app.author')),
            ],
        ),
    ]

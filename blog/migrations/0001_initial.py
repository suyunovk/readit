# Generated by Django 5.0.4 on 2024-04-24 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamStamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=212)),
                ('image', models.ImageField(blank=True, upload_to='author')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('teamstamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.teamstamp')),
                ('title', models.CharField(max_length=212)),
                ('image', models.ImageField(upload_to='images/')),
                ('video', models.FileField(upload_to='videos/')),
                ('description', models.TextField()),
                ('description_missin', models.TextField()),
                ('description_vision', models.TextField()),
                ('description_value', models.TextField()),
            ],
            bases=('blog.teamstamp',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('teamstamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.teamstamp')),
                ('title', models.CharField(max_length=40)),
            ],
            bases=('blog.teamstamp',),
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('teamstamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.teamstamp')),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
            bases=('blog.teamstamp',),
        ),
        migrations.CreateModel(
            name='HappyClients',
            fields=[
                ('teamstamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.teamstamp')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('full_name', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
            ],
            bases=('blog.teamstamp',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('teamstamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.teamstamp')),
                ('title', models.CharField(max_length=40)),
            ],
            bases=('blog.teamstamp',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('teamstamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.teamstamp')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('message', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
            ],
            bases=('blog.teamstamp',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('twitter', models.CharField(max_length=200)),
                ('facebook', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
                ('tags', models.ManyToManyField(to='blog.tag')),
            ],
        ),
    ]

# Generated by Django 4.1.1 on 2023-04-30 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(max_length=200, unique=True)),
                ('community_description', models.TextField()),
                ('community_image', models.ImageField(upload_to='community_imgs/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communities', to='base.community')),
            ],
        ),
    ]
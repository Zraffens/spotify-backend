# Generated by Django 4.0.6 on 2023-06-05 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artist', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(null=True, upload_to='musics/')),
                ('liked', models.BooleanField(default=False)),
                ('length', models.PositiveIntegerField(blank=True, null=True)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artist.artist')),
            ],
        ),
    ]

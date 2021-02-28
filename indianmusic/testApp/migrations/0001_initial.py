# Generated by Django 2.1 on 2021-02-27 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistimage', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('artistname', models.CharField(max_length=128)),
                ('song', models.FileField(blank=True, null=True, upload_to='')),
                ('songname', models.CharField(max_length=200)),
                ('duration', models.FloatField()),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['uploaded'],
            },
        ),
    ]
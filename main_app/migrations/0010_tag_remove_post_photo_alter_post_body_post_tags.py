# Generated by Django 4.1.7 on 2023-03-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_post_photo_alter_photo_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='main_app.tag'),
        ),
    ]
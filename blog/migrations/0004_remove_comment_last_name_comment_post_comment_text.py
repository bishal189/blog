# Generated by Django 4.2.3 on 2023-07-27 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='last_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=400, null=True),
        ),
    ]

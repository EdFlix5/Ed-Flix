# Generated by Django 3.1.4 on 2021-05-02 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_fileupload_file_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='file_name',
            field=models.CharField(default='abc', max_length=100),
            preserve_default=False,
        ),
    ]

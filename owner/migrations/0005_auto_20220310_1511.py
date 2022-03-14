# Generated by Django 3.2.12 on 2022-03-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_auto_20220308_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='city',
            new_name='destination',
        ),
        migrations.AddField(
            model_name='car',
            name='startpoint',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

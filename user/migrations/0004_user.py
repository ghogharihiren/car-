# Generated by Django 3.2.12 on 2022-03-04 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=10)),
                ('addreaa', models.TextField(max_length=100)),
                ('pic', models.FileField(default='1.png', upload_to='profile')),
            ],
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-10 14:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='颜色不符合规范', regex='^(yellow|blue|red|green)$')], verbose_name='鞋子颜色')),
                ('size', models.IntegerField(max_length=10, verbose_name='鞋子大小')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='用户姓名')),
                ('phone', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='手机号不符合规范', regex='^(138|176|184)\\d{8}$')], verbose_name='用户手机')),
            ],
        ),
        migrations.AddField(
            model_name='shoes',
            name='shoes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bg.User'),
        ),
    ]

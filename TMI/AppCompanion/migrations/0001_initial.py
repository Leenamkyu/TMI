# Generated by Django 2.2.1 on 2019-08-07 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('모집중', '모집중'), ('모집완료', '모집완료')], max_length=100)),
                ('category', models.CharField(choices=[('음식', '음식'), ('액티비티', '액티비티'), ('관광', '관광'), ('힐링', '힐링')], max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('bucket_list', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
        ),
    ]

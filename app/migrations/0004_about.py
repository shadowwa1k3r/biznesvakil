# Generated by Django 2.2.9 on 2019-12-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191222_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_uz', models.TextField()),
                ('header_ru', models.TextField()),
                ('header_en', models.TextField()),
                ('title_uz', models.TextField()),
                ('title_ru', models.TextField()),
                ('title_en', models.TextField()),
                ('content_ru', models.TextField()),
                ('content_en', models.TextField()),
                ('content_uz', models.TextField()),
            ],
            options={
                'db_table': 'about',
            },
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_text', models.CharField(max_length=50)),
                ('word_type', models.CharField(max_length=50)),
                ('word_trans', models.CharField(max_length=200)),
            ],
        ),
    ]
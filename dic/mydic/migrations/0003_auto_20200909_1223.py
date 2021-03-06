# Generated by Django 3.1.1 on 2020-09-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydic', '0002_word_word_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='word_date',
            field=models.DateTimeField(verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_text',
            field=models.CharField(max_length=50, verbose_name='Word'),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_trans',
            field=models.CharField(max_length=200, verbose_name='Translation'),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_type',
            field=models.CharField(max_length=50, verbose_name='Type'),
        ),
    ]

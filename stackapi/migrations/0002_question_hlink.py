# Generated by Django 2.1.1 on 2019-04-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hlink',
            field=models.CharField(default='/', max_length=250),
            preserve_default=False,
        ),
    ]

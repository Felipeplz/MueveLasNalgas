# Generated by Django 3.2.4 on 2021-07-01 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muevelasnalgas', '0002_auto_20210701_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='zona',
            name='nombre',
            field=models.CharField(default='Test', max_length=100),
            preserve_default=False,
        ),
    ]

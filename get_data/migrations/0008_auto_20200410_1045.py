# Generated by Django 2.2.7 on 2020-04-10 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_data', '0007_candidate_attend'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='promise1',
            field=models.TextField(blank=True, verbose_name='교육'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='promise2',
            field=models.TextField(blank=True, verbose_name='재난/코로나'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='promise3',
            field=models.TextField(blank=True, verbose_name='여성/노인/장애인/어린이'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='promise4',
            field=models.TextField(blank=True, verbose_name='도시개발'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='promise5',
            field=models.TextField(blank=True, verbose_name='소상공인/자영업자'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='promise6',
            field=models.TextField(blank=True, verbose_name='청년/일자리'),
        ),
    ]

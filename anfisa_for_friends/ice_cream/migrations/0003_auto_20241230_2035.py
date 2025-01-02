# Generated by Django 3.2.16 on 2024-12-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_auto_20241223_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='output_order',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения'),
        ),
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(help_text='Уникальное название категории, не более 256 символов', max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='wrapper',
            name='title',
            field=models.CharField(help_text='Уникальное название обёртки, не более 256 символов', max_length=256, verbose_name='Название'),
        ),
    ]
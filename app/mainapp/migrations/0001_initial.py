# Generated by Django 2.1.7 on 2019-03-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('title_internal', models.CharField(help_text='Отображается только в адм.части', max_length=200, verbose_name='Название')),
                ('button_url', models.URLField(blank=True, verbose_name='Ссылка')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'слайдер',
                'verbose_name_plural': 'слайдеры',
            },
        ),
    ]

# Generated by Django 2.0.8 on 2019-04-02 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20190402_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.IntegerField(choices=[(1, 'Главная'), (2, 'Контакты'), (3, 'Общий')], verbose_name='День недели')),
            ],
            options={
                'verbose_name': 'Шаблон',
                'verbose_name_plural': 'Шаблоны',
            },
        ),
        migrations.AddField(
            model_name='page',
            name='template',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.Template', verbose_name='Шаблон'),
        ),
    ]

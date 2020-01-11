# Generated by Django 3.0.2 on 2020-01-11 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20170516_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='page',
            name='modification_date',
        ),
        migrations.AddField(
            model_name='page',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('hy', 'Armenian'), ('nl', 'Dutch'), ('ru', 'Russian'), ('de', 'German'), ('fr', 'French')], default='en', max_length=10, verbose_name='language'),
        ),
        migrations.AddField(
            model_name='page',
            name='translation_of',
            field=models.ForeignKey(blank=True, help_text='Leave this empty for entries in the primary language.', limit_choices_to={'language': 'en'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='page.Page', verbose_name='translation of'),
        ),
        migrations.AlterField(
            model_name='page',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='page',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='page',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
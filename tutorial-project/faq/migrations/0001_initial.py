# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import aldryn_apphooks_config.fields
import app_data.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('question', models.TextField(blank=True, default='')),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='FaqConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('type', models.CharField(max_length=100, verbose_name='type')),
                ('namespace', models.CharField(default=None, unique=True, max_length=100, verbose_name='instance namespace')),
                ('app_data', app_data.fields.AppDataField(editable=False, default='{}')),
                ('paginate_by', models.PositiveIntegerField(default=5, verbose_name='Paginate size')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Apphook configs',
                'verbose_name': 'Apphook config',
            },
        ),
        migrations.AlterUniqueTogether(
            name='faqconfig',
            unique_together=set([('type', 'namespace')]),
        ),
        migrations.AddField(
            model_name='entry',
            name='app_config',
            field=aldryn_apphooks_config.fields.AppHookConfigField(help_text='When selecting a value, the form is reloaded to get the updated default', to='faq.FaqConfig'),
        ),
    ]

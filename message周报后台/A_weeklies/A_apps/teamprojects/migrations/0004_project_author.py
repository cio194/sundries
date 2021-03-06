# Generated by Django 2.0.1 on 2019-07-14 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teamprojects', '0003_auto_20190710_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-27 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_category_name_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.PROTECT, related_name='articles', to='main.category'),
            preserve_default=False,
        ),
    ]
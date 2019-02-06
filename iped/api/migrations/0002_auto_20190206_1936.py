# Generated by Django 2.1.5 on 2019-02-06 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='produto',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produto', to='api.Produto'),
        ),
    ]

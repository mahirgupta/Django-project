# Generated by Django 3.2.12 on 2022-05-16 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_desc', models.CharField(max_length=200)),
                ('item_price', models.IntegerField()),
                ('item_url', models.CharField(default='data:image/jpeg;base64,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', max_length=500)),
            ],
        ),
    ]
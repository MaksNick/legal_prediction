# Generated by Django 4.2.9 on 2024-04-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0002_queryhistory_predicted_outcome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queryhistory',
            name='query_text',
            field=models.TextField(max_length=255),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-19 09:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('imagesColor', models.CharField(max_length=50)),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.productimage')),
            ],
        ),
    ]

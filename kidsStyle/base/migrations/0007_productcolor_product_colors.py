# Generated by Django 4.2.5 on 2023-09-19 08:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_product_brand_alter_product_sizes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('colorCode', models.CharField(max_length=50, unique=True)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(blank=True, to='base.productcolor'),
        ),
    ]

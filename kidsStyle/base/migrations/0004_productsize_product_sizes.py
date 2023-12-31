# Generated by Django 4.2.5 on 2023-09-19 07:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(blank=True, to='base.productsize'),
        ),
    ]

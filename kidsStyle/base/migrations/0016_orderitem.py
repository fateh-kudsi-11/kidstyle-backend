# Generated by Django 4.2.5 on 2023-10-13 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0015_alter_productdetails_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('qty', models.PositiveIntegerField(default=1)),
                ('selected_color', models.CharField(max_length=255)),
                ('selected_size', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
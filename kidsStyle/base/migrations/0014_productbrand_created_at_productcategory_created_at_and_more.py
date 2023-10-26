# Generated by Django 4.2.5 on 2023-09-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_productcategory_producttype_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbrand',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='productcolor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='productimage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='productsize',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='producttype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

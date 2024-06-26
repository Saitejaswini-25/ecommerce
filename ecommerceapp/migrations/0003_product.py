# Generated by Django 5.0.6 on 2024-06-03 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_rename_desc_contact_message_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('category', models.CharField(default='', max_length=100)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('coins', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='images/images')),
            ],
        ),
    ]

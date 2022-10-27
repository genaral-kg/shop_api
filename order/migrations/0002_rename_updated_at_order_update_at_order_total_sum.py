# Generated by Django 4.1.2 on 2022-10-25 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='updated_at',
            new_name='update_at',
        ),
        migrations.AddField(
            model_name='order',
            name='total_sum',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
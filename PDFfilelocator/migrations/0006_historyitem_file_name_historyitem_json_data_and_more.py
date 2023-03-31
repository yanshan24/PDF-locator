# Generated by Django 4.1.7 on 2023-03-31 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PDFfilelocator', '0005_historyitem_authorid_alter_field_history_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyitem',
            name='file_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historyitem',
            name='json_data',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='historyitem',
            name='pdf_file',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='Field',
        ),
    ]

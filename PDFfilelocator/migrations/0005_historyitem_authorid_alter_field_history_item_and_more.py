# Generated by Django 4.1.7 on 2023-03-30 22:40

import PDFfilelocator.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PDFfilelocator', '0004_pdffile_historyitem_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyitem',
            name='authorID',
            field=models.CharField(default=PDFfilelocator.models.uuid_hex, max_length=40),
        ),
        migrations.AlterField(
            model_name='field',
            name='history_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='PDFfilelocator.historyitem'),
        ),
        migrations.AlterField(
            model_name='historyitem',
            name='pdf_file',
            field=models.FileField(upload_to=''),
        ),
        migrations.DeleteModel(
            name='PDFFile',
        ),
    ]
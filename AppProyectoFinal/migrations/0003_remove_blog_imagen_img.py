# Generated by Django 4.1 on 2022-10-19 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoFinal', '0002_alter_blog_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='imagen',
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProyectoFinal.blog')),
            ],
        ),
    ]

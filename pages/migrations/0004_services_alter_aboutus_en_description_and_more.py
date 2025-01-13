# Generated by Django 4.2.17 on 2025-01-12 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_aboutus_options_alter_photoslider_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_title', models.CharField(max_length=200, verbose_name='English title')),
                ('fa_title', models.CharField(max_length=200, verbose_name='Persian title')),
                ('en_description', models.TextField(verbose_name='English description')),
                ('fa_description', models.TextField(verbose_name='Persian description')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Services',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='en_description',
            field=models.TextField(verbose_name='English description'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='en_title',
            field=models.CharField(help_text='For display in database tables only. The main title is in the section title section.', max_length=200, verbose_name='English title'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='fa_description',
            field=models.TextField(verbose_name='Persian description'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='fa_title',
            field=models.CharField(help_text='For display in database tables only. The main title is in the section title section.', max_length=200, verbose_name='Persian title'),
        ),
        migrations.AlterField(
            model_name='photoslider',
            name='en_text',
            field=models.TextField(verbose_name='English text'),
        ),
        migrations.AlterField(
            model_name='photoslider',
            name='en_title',
            field=models.CharField(max_length=100, verbose_name='English title'),
        ),
        migrations.AlterField(
            model_name='photoslider',
            name='fa_text',
            field=models.TextField(verbose_name='Persian text'),
        ),
        migrations.AlterField(
            model_name='photoslider',
            name='fa_title',
            field=models.CharField(max_length=100, verbose_name='Persian title'),
        ),
        migrations.AlterField(
            model_name='photoslider',
            name='image',
            field=models.ImageField(help_text='Used to display in the background of a slide.', upload_to='slider/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='photoslider',
            name='order',
            field=models.SmallIntegerField(help_text='Specify the slide display order, which slide should be the first.', verbose_name='Display order'),
        ),
    ]

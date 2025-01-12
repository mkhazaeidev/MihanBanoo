# Generated by Django 4.2.17 on 2025-01-12 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('preferences', '0003_websitedetails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='websitedetails',
            options={'verbose_name': 'WebsiteDetails', 'verbose_name_plural': 'WebsiteDetails'},
        ),
        migrations.RemoveField(
            model_name='websiteowner',
            name='strat_work_time',
        ),
        migrations.AddField(
            model_name='websiteowner',
            name='start_work_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Start work time'),
        ),
        migrations.AlterField(
            model_name='websitedetails',
            name='description',
            field=models.CharField(blank=True, help_text='A brief explanation of the goals of the site.', max_length=400, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='websitedetails',
            name='logo_image',
            field=models.ImageField(blank=True, null=True, upload_to='website/images/logo/', verbose_name='Logo Image'),
        ),
        migrations.AlterField(
            model_name='websitedetails',
            name='logo_touch_icon',
            field=models.ImageField(blank=True, null=True, upload_to='website/images/logo/', verbose_name='Logo Touch icon'),
        ),
        migrations.AlterField(
            model_name='websitedetails',
            name='main_title',
            field=models.CharField(blank=True, help_text='The name that is used as the main name of the site or as the site logo.', max_length=200, verbose_name='Main Title'),
        ),
        migrations.AlterField(
            model_name='websitedetails',
            name='page_title',
            field=models.CharField(blank=True, help_text='The name that appears at the top of the page as the title.', max_length=100, verbose_name='Page Title'),
        ),
        migrations.AlterField(
            model_name='websitedetails',
            name='seo_keyword',
            field=models.CharField(blank=True, help_text='Keywords to help Google search engine.', max_length=400, verbose_name='SEO Keywords'),
        ),
        migrations.AlterField(
            model_name='websiteowner',
            name='end_work_day',
            field=models.CharField(blank=True, choices=[('1', 'Saturday'), ('2', 'Sunday'), ('3', 'Monday'), ('4', 'Tuesday'), ('5', 'Wednesday'), ('6', 'Thursday'), ('7', 'Friday')], max_length=1, null=True, verbose_name='Last working day of the week'),
        ),
        migrations.AlterField(
            model_name='websiteowner',
            name='end_work_time',
            field=models.TimeField(blank=True, null=True, verbose_name='End work time'),
        ),
        migrations.AlterField(
            model_name='websiteowner',
            name='owner',
            field=models.OneToOneField(help_text='Select the site owner from among users to display contact information.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Website Owner'),
        ),
        migrations.AlterField(
            model_name='websiteowner',
            name='start_work_day',
            field=models.CharField(blank=True, choices=[('1', 'Saturday'), ('2', 'Sunday'), ('3', 'Monday'), ('4', 'Tuesday'), ('5', 'Wednesday'), ('6', 'Thursday'), ('7', 'Friday')], max_length=1, null=True, verbose_name='The first working day of the week'),
        ),
    ]

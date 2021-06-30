# Generated by Django 3.2.4 on 2021-06-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='at',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('AllCategoriesAppearedBoys', models.IntegerField()),
                ('AllCategoriesAppearedGirls', models.IntegerField()),
                ('AllCategoriesTotal', models.IntegerField()),
                ('AllCategoriesPassedBoys', models.IntegerField()),
                ('AllCategoriesPassedGirls', models.IntegerField()),
                ('AllCategoriesPassedTotal', models.IntegerField()),
                ('ScheduledCasteStudentsAppearedBoys', models.IntegerField()),
                ('ScheduledCasteStudentsAppearedGirls', models.IntegerField()),
                ('ScheduledCasteStudentsAppearedTotal', models.IntegerField()),
                ('ScheduledCasteStudentsPassedBoys', models.IntegerField()),
                ('ScheduledCasteStudentsPassedGirls', models.IntegerField()),
                ('ScheduledCasteStudentsPassedTotal', models.IntegerField()),
                ('ScheduledTribeStudentsAppearedBoys', models.IntegerField()),
                ('ScheduledTribeStudentsAppearedGirls', models.IntegerField()),
                ('ScheduledTribeStudentsAppearedTotal', models.IntegerField()),
                ('ScheduledTribeStudentsPassedBoys', models.IntegerField()),
                ('ScheduledTribeStudentsPassedGirls', models.IntegerField()),
                ('ScheduledTribeStudentsPassedTotal', models.IntegerField()),
            ],
        ),
    ]

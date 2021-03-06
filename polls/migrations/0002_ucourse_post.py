# Generated by Django 3.1.2 on 2020-12-22 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='uCourse_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.course')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.post')),
            ],
            options={
                'unique_together': {('course', 'post')},
            },
        ),
    ]

# Generated by Django 3.1.2 on 2020-12-22 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('Name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Photo', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Picture', models.CharField(max_length=25)),
                ('Explanation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='File2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Header_photo', models.CharField(max_length=25)),
                ('Create_time', models.DateTimeField(auto_now_add=True)),
                ('Summary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Photo', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='polls.post')),
                ('Content1', models.CharField(max_length=30)),
                ('Content2', models.CharField(max_length=20)),
                ('Main_content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='Writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user'),
        ),
        migrations.AddField(
            model_name='post',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.categories'),
        ),
        migrations.CreateModel(
            name='ReadsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user')),
            ],
            options={
                'unique_together': {('user', 'post')},
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user')),
            ],
            options={
                'unique_together': {('user', 'post')},
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user')),
            ],
            options={
                'unique_together': {('user', 'post')},
            },
        ),
        migrations.CreateModel(
            name='Course_Post2',
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

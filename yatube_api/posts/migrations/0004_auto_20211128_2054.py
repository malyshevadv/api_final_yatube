# Generated by Django 2.2.16 on 2021-11-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20211128_1954'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follow',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_follow'),
        ),
    ]

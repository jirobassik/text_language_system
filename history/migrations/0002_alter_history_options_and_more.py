# Generated by Django 5.0.3 on 2024-03-29 10:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="history",
            options={"ordering": ["-created_at"]},
        ),
        migrations.RemoveIndex(
            model_name="history",
            name="history_his_created_76cef1_idx",
        ),
        migrations.RenameField(
            model_name="history",
            old_name="created_add",
            new_name="created_at",
        ),
        migrations.AddIndex(
            model_name="history",
            index=models.Index(
                fields=["created_at", "is_deleted"],
                name="history_his_created_f5630c_idx",
            ),
        ),
    ]

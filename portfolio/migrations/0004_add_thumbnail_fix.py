from django.db import migrations
import cloudinary.models

class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_heroslide_image_alter_heroslide_video_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(
                'image',
                max_length=255,
                blank=True,
                null=True
            ),
        ),
    ]

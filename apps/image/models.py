import uuid
from datetime import datetime

from django.db import models


def rename_image(instance, filename):
    new_image_name = uuid.uuid4()
    current_date = datetime.now()
    year = current_date.year
    month = current_date.month
    day = current_date.day
    return f'images/{year}/{month}/{day}/{new_image_name}.{filename.split(".")[-1]}'


class Image(models.Model):
    image_url = models.ImageField(upload_to=rename_image)

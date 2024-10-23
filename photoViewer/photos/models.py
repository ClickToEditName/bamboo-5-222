from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    location = models.CharField(max_length=255)
    capture_date = models.DateField()  # ʹ�� DateField �洢�����ո�ʽ

    def __str__(self):
        return f"{self.image.name} - {self.location} - {self.capture_date}"

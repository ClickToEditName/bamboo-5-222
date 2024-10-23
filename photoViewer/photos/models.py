from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    location = models.CharField(max_length=255)
    capture_date = models.DateField()  # 使用 DateField 存储年月日格式

    def __str__(self):
        return f"{self.image.name} - {self.location} - {self.capture_date}"

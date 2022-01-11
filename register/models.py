from django.db import models


# Create your models here.
class Person(models.Model):

    # 修改介面順序的地方
    name = models.CharField(max_length=15, blank=False) 
    tel = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=25, blank=False)
    data = models.CharField(max_length=5, blank=False)
    time = models.CharField(max_length=5, blank=False)
    WAY_CHOICES = [
        ('Store', '店取'),
        ('Home', '宅配'),
    ]
    way_id = models.CharField(max_length=5, choices = WAY_CHOICES, default='Store')

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name

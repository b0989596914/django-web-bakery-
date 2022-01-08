from django.db import models

class Opinion(models.Model):

    name = models.CharField(max_length=10, blank=False) 
    # text = models.CharField(max_length=100, blank=False)
    text = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name
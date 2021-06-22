from django.db import models


# Create your models here.
class blog(models.Model):
    Name = models.CharField(max_length=50)
    Text = models.TextField()

    def __str__(self):
        return self.Name

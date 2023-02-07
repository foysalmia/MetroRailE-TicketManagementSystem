from django.db import models

# Create your models here.

class server(models.Model):
    email = models.CharField( max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.email

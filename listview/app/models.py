from django.db import models

# Create your models here.


class School(models.Model):
    name=models.CharField(max_length=30)
    Princ=models.CharField(max_length=20)
    loc=models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name
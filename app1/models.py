from django.contrib.auth.models import User
from django.db import models

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField()
    kasb = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism


class Maqola(models.Model):
    sarlavha = models.CharField(max_length=50)
    sana = models.DateField(auto_now_add=True)
    mavzu = models.CharField(max_length=50)
    matn = models.CharField(max_length=200)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha
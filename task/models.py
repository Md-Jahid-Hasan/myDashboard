from django.db import models
from django.contrib.auth import get_user_model as User


class Place(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class DailyCost(models.Model):
    user = models.ForeignKey(User(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    purpose = models.CharField(max_length=250)
    is_refundable = models.BooleanField(default=False)
    place = models.ForeignKey(Place, on_delete=models.RESTRICT)


class Task(models.Model):
    user = models.ForeignKey(User(), on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    work = models.CharField(max_length=250)
    place = models.ForeignKey(Place, on_delete=models.RESTRICT, blank=True, null=True)






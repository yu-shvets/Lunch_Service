from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.user)


class Item(models.Model):

    class Meta(object):
        verbose_name = "Item"
        verbose_name_plural = "Items"

    name = models.CharField(max_length=256)
    price = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)


class Order(models.Model):

    class Meta(object):
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['-datetime']

    datetime = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    def calculate_total(self):
        return sum(item.price for item in self.items.all())

    def __str__(self):
        return "{}-{}".format(self.user, self.datetime)



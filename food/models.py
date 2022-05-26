from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class item(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_url = models.CharField(max_length=10000, default="https://cdn.pixabay.com/photo/2019/09/08/17/24/eat-4461470_1280.png")

    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"item_id": self.pk})
    
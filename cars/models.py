from django.db import models
from django.forms import IntegerField
from dealers.models import Dealer
from django.urls import reverse

# Create your models here.

class Car(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.DO_NOTHING)
    brand = models.CharField(max_length=100)
    CATEGORY=(
        ('New','New'),
        ('Used','Used')
    )
    category = models.CharField(max_length=50,choices=CATEGORY)
    image_main = models.ImageField(upload_to='images')

    miles = models.IntegerField(blank=True, null=True)
    
    TRANSMISSION =(
        ('Manual','Manual'),
        ('Automatic','Automatic')
    )
    transmission = models.CharField(max_length=50,choices=TRANSMISSION)
    year = models.IntegerField()
    power = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('car_detail',kwargs={
            'car_id':self.id
        })


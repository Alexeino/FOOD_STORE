from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, SlugField
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "City Enteries"

    def __str__(self):
        return f"{self.name} ({self.code})"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=8)
    city = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Adress Enteries"

    def __str__(self):
        return f"{self.street} {self.city}, {self.postal_code}"

class Sheff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100,blank=True)
    address = models.OneToOneField(Address,on_delete=CASCADE, null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.address}"

class Food(models.Model):
    dish = models.CharField(max_length=100)
    rating = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    is_popular = BooleanField(default=False)
    sheff = models.ForeignKey(Sheff, on_delete=models.CASCADE,related_name="foods")
    slug = SlugField(default="",blank=True,null=False,db_index=True)
    origin_city = models.ManyToManyField(City)


    def __str__(self):
        return f"[{self.id}.]       {self.dish}, Rating:{self.rating}"
    
    # def save(self, *args,**kwargs):
    #     self.slug = slugify(self.dish)

    #     super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("food_detail",args=[self.slug])



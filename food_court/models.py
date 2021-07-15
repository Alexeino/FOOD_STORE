from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models.fields import BooleanField, SlugField
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Food(models.Model):
    dish = models.CharField(max_length=100)
    rating = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    is_popular = BooleanField(default=False)
    slug = SlugField(default="",null=False,db_index=True)


    def __str__(self):
        return f"[{self.id}.]       {self.dish}, Rating:{self.rating}"
    
    def save(self, *args,**kwargs):
        self.slug = slugify(self.dish)

        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("food_detail",args=[self.slug])

    
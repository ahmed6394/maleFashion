from django.db import models
from django.core.validators import validate_email

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(null=True, blank=True, upload_to="images/")
    price = models.FloatField(null=True, blank=True)
    ratings = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[validate_email])
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
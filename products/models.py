from django.db import models
import uuid

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    featured_image = models.ImageField(default='default.jpg')
    price = models.FloatField(null=True, blank=True, default=0)
    min_order= models.IntegerField(default=1)
    stock = models.IntegerField(default=0)
    exp_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL, default=None)
    tags = models.ManyToManyField("Tag", blank=True)
    # edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    
    
    def __str__(self) -> str:
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    
    def __str__(self) -> str:
        return self.name


class Feedback(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
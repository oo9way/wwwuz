from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

def generate_key():
    key = get_random_string(length=17)
    return key

# Categories
class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    

# Website 
class Website(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    api_key = models.CharField(max_length=17, default=generate_key, unique=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)



# Unique visitor
class Visitor(models.Model):
    visitor_hash = models.CharField(max_length=512)
    website = models.ForeignKey(Website, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)



# Daily visitors count
class Data(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)

    date = models.DateField(auto_now_add=True)
    visitors = models.IntegerField(default=0)
    unique_visitors = models.IntegerField(default=0)


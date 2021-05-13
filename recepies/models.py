from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Recepies(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    description = models.TextField()
    ingredients = models.TextField()
    cooking_guide = models.TextField()
    categories = models.ManyToManyField('Category', related_name='recepies')

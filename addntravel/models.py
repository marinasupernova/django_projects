from django.db import models

class Travel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    destination = models.TextField()
    season = models.TextField()
    description = models.TextField()

    
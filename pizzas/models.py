from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length= 200)

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete= models.CASCADE)
    topping_name = models.CharField(max_length= 200)

    def __str__(self):
        return f"{self.topping_name[:50]}..."
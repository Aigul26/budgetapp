from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.IntegerField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.owner)+'s project'

class Category(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)

class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)



class Income(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='incomes')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)



def __str__(self):
    return str(self.owner) + 's project'
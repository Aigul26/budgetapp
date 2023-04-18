from django.contrib import admin
from .models import  Project, Expense, Category, Income

admin.site.register(Project)
admin.site.register(Expense)
admin.site.register(Category)
admin.site.register(Income)
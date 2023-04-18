from rest_framework import serializers
from .models import Expense, Project, Income

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'slug', 'budget']

class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ['id', 'project', 'date', 'title', 'amount', 'category']

class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = ['id', 'project', 'date', 'title', 'amount']
from django import forms


class ExpenseForm(forms.Form):
    title = forms.CharField()
    amount = forms.IntegerField()
    category = forms.CharField()
    date = forms.DateField()



class BalanseForm(forms.Form):
    income_title = forms.CharField()
    income_amount = forms.IntegerField()
    date = forms.DateField()

from django import forms
from .models import Expenses

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['name', 'cost', 'expense_date']
        widgets = {
            'expense_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

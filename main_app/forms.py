from django import forms
from .models import Expenses
from .models import Car
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

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_id', 'brand', 'name', 'year_model', 'type', 'buy_date', 'buy_price', 'status', 'description', 'image']
        widgets = {
            'buy_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'placeholder': 'Select a date'
                }
            )
        }
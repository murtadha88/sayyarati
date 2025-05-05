from django import forms
from .models import Expenses
from .models import Car
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput()
    )
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput()
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
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
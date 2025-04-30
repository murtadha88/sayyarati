from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Car
from .forms import ExpensesForm

from .models import Car
class Login(LoginView):
    template_name = 'login.html'


def home(request):
    return render(request, 'base.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    expenses_form = ExpensesForm()
    return render(request, 'cars/details.html', {'car': car , 'expenses_form': expenses_form})

def add_expenses(request, car_id):
    form = ExpensesForm(request.POST)
    if form.is_valid():
        new_expenses = form.save(commit=False)
        new_expenses.car_id = car_id
        new_expenses.save()

        car = Car.objects.get(id=car_id)
        car.total_cost += new_expenses.cost
        car.save()

    return redirect('car-detail', car_id=car_id)
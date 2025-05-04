from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from .models import Car, Expenses
from .forms import ExpensesForm
from .forms import CarForm
from django.utils import timezone


from .models import Car
class Login(LoginView):
    template_name = 'login.html'

class CarCreate(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = '/cars/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.total_cost = form.cleaned_data['buy_price']  
        return super().form_valid(form)

class CarUpdate(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = 'cars/car_confirm_delete.html'

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

def cars_history(request):
    cars = Car.objects.all()
    return render(request, 'cars/history.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)

    edit_expense = None
    expenses_form = ExpensesForm()

    edit_id = request.GET.get('edit_expense_id')
    if edit_id:
        edit_expense = Expenses.objects.get(id=edit_id, car_id=car_id)
        expenses_form = ExpensesForm(instance=edit_expense)

    context = {
        'car': car,
        'expenses_form': expenses_form,
        'editing': edit_expense is not None,
        'edit_expense_id': edit_id,
    }
    return render(request, 'cars/details.html', context)


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

def update_expense_inline(request, car_id, pk):
    expense = Expenses.objects.get(pk=pk, car_id=car_id)
    if request.method == 'POST':
        form = ExpensesForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('car-detail', car_id=car_id)
    else:
        return redirect(f'/cars/{car_id}/?edit_expense_id={pk}')


class ExpenseDelete(DeleteView):
    model = Expenses
    context_object_name = 'expense'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_id'] = self.kwargs['car_id']
        return context

    def get_success_url(self):
        return f'/cars/{self.kwargs["car_id"]}/'
    

def sell_car(request, car_id):
    car = Car.objects.get(id=car_id)

    if request.method == 'POST':
        sell_price = float(request.POST.get('sell_price'))

        profit = sell_price - car.total_cost
        profit_percentage = (profit / car.total_cost) * 100

        car.sell_price = sell_price
        car.profit = profit
        car.profit_percentage = profit_percentage
        car.sell_date = timezone.now()
        car.status = 'Sold'
        car.save()

    return redirect('car-detail', car_id=car_id)

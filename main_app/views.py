from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from .models import Car

from .models import Car
class Login(LoginView):
    template_name = 'login.html'

class CarCreate(CreateView):
    model = Car
    fields = ['car_id','brand','name','year_model','type','buy_date','buy_price','status','description','image']
    template_name = 'cars/car_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.total_cost = form.cleaned_data['buy_price']  
        return super().form_valid(form)
    
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
    return render(request, 'cars/details.html', {'car': car})

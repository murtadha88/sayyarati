from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.
TYPE = (
    "Sedan",
    "SUV",
    "Coupe",
    "Hatchback",
    "Convertible",
    "Pickup Truck",
    "Van",
    "Minivan",
    "Wagon",
    "Crossover",
    "Sports Car",
    "Electric Car",
    "Hybrid Car",
    "Luxury Car",
    "Off-Road Vehicle"
)
STATUS=(
    'Available to Sale',
    'In Inventory',
    'Sold'
)
BRANDS = (
    "Toyota",
    "Honda",
    "Ford",
    "Chevrolet",
    "Mercedes-Benz",
    "BMW",
    "Audi",
    "Volkswagen",
    "Hyundai",
    "Nissan",
    "Kia",
    "Lexus",
    "Mazda",
    "Subaru",
    "Jeep",
    "Dodge",
    "Ram",
    "Porsche",
    "Ferrari",
    "Lamborghini",
    "Mitsubishi",
    "Peugeot",
    "Renault",
    "Volvo",
    "Land Rover",
    "Jaguar",
    "Mini",
    "Chrysler",
    "GMC",
    "Acura",
    "Infiniti",
    "Genesis",
    "Alfa Romeo",
    "Suzuki",
    "Tata Motors",
    "Saab",
    "Skoda",
    "Pagani",
    "Bentley",
    "Rolls-Royce",
    "Maserati",
    "Bugatti",
    "Tesla",
    "Lucid Motors",
    "BYD",
    "Geely",
    "Changan",
    "Perodua",
    "Haval"
)

class Car(models.Model):
    car_id = models.IntegerField(max_length=6)
    brand = models.CharField(
        choices=BRANDS,
        default=BRANDS[0]
    )
    name = models.CharField(max_length=100)
    image = models.ImageField()
    year_model = models.IntegerField(max_length=4)
    type=models.CharField(
        choices=TYPE,
        default=TYPE[0]
    )
    description = models.TextField()
    buy_date = models.DateField()
    sell_date = models.DateField()
    buy_price = models.FloatField()
    total_cost = models.FloatField()
    profit = models.FloatField()
    profit_percentage = models.FloatField()
    status =  models.CharField(
        choices=STATUS,
        default=STATUS[0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_id
    

class Expenses(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField()
    expense_date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
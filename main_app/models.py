from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
TYPE = (
    ("Sedan", "Sedan"),
    ("SUV", "SUV"),
    ("Coupe", "Coupe"),
    ("Hatchback", "Hatchback"),
    ("Convertible", "Convertible"),
    ("Pickup Truck", "Pickup Truck"),
    ("Van", "Van"),
    ("Minivan", "Minivan"),
    ("Wagon", "Wagon"),
    ("Crossover", "Crossover"),
    ("Sports Car", "Sports Car"),
    ("Electric Car", "Electric Car"),
    ("Hybrid Car", "Hybrid Car"),
    ("Luxury Car", "Luxury Car"),
    ("Off-Road Vehicle", "Off-Road Vehicle"),
)

STATUS = (
    ("Available to Sale", "Available to Sale"),
    ("In Inventory", "In Inventory"),
    ("Sold", "Sold"),
)

BRANDS = (
    ("Toyota", "Toyota"),
    ("Honda", "Honda"),
    ("Ford", "Ford"),
    ("Chevrolet", "Chevrolet"),
    ("Mercedes-Benz", "Mercedes-Benz"),
    ("BMW", "BMW"),
    ("Audi", "Audi"),
    ("Volkswagen", "Volkswagen"),
    ("Hyundai", "Hyundai"),
    ("Nissan", "Nissan"),
    ("Kia", "Kia"),
    ("Lexus", "Lexus"),
    ("Mazda", "Mazda"),
    ("Subaru", "Subaru"),
    ("Jeep", "Jeep"),
    ("Dodge", "Dodge"),
    ("Ram", "Ram"),
    ("Porsche", "Porsche"),
    ("Ferrari", "Ferrari"),
    ("Lamborghini", "Lamborghini"),
    ("Mitsubishi", "Mitsubishi"),
    ("Peugeot", "Peugeot"),
    ("Renault", "Renault"),
    ("Volvo", "Volvo"),
    ("Land Rover", "Land Rover"),
    ("Jaguar", "Jaguar"),
    ("Mini", "Mini"),
    ("Chrysler", "Chrysler"),
    ("GMC", "GMC"),
    ("Acura", "Acura"),
    ("Infiniti", "Infiniti"),
    ("Genesis", "Genesis"),
    ("Alfa Romeo", "Alfa Romeo"),
    ("Suzuki", "Suzuki"),
    ("Tata Motors", "Tata Motors"),
    ("Saab", "Saab"),
    ("Skoda", "Skoda"),
    ("Pagani", "Pagani"),
    ("Bentley", "Bentley"),
    ("Rolls-Royce", "Rolls-Royce"),
    ("Maserati", "Maserati"),
    ("Bugatti", "Bugatti"),
    ("Tesla", "Tesla"),
    ("Lucid Motors", "Lucid Motors"),
    ("BYD", "BYD"),
    ("Geely", "Geely"),
    ("Changan", "Changan"),
    ("Perodua", "Perodua"),
    ("Haval", "Haval"),
)


class Car(models.Model):
    car_id = models.IntegerField()
    brand = models.CharField(
        max_length=50,
        choices=BRANDS,
        default=BRANDS[0][0]
    )
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)
    year_model = models.IntegerField()
    type=models.CharField(
        max_length=50,
        choices=TYPE,
        default=TYPE[0][0]
    )
    description = models.TextField()
    buy_date = models.DateField()
    sell_date = models.DateField(null=True, blank=True)
    buy_price = models.FloatField()
    sell_price = models.FloatField(null=True, blank=True)
    total_cost = models.FloatField()
    profit = models.FloatField(null=True, blank=True)
    profit_percentage = models.FloatField(null=True, blank=True)
    status =  models.CharField(
        max_length=50,
        choices=STATUS,
        default=STATUS[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.name} ({self.car_id})"
    
    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'car_id': self.id})
    
class Expenses(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField()
    expense_date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ['-expense_date']
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.Login.as_view(), name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('cars/', views.cars, name='cars'),
    path('cars/<int:car_id>/', views.car_detail, name='car-detail'),
    path('cars/create/', views.CarCreate.as_view(), name='car-create'),
    path(
        'cars/<int:car_id>/add-expenses/', 
        views.add_expenses, 
        name='add-expenses'
    ),
    path('cars/<int:car_id>/expenses/<int:pk>/edit/', views.update_expense_inline, name='update-expense-inline'),
    path('cars/<int:car_id>/expenses/<int:pk>/delete/', views.ExpenseDelete.as_view(), name='expense-delete'),
    path('cars/<int:car_id>/sell/', views.sell_car, name='sell-car'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views

urlpatterns = [
    path('Login/', views.load_login, name="login"),
    path('Login/Customer/<int:id>/', views.load_customer, name="customer"),
    path('Login/Waiter/<int:id>/', views.load_waiter),
    path('Login/Chef/<int:id>/', views.load_chef),
    path('update_stock/<int:item_id>/<int:id>/<str:operation>/', views.update_stock, name='update_stock'),
    path('update_order/<int:order_number>/<int:id>/<str:operation>/', views.update_order, name='update_order'),
    path('update_order_waiter/<int:order_number>/<int:id>/<str:operation>/', views.update_order_waiter, name='update_order_waiter'),


]

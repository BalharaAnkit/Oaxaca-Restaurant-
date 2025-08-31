from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_login, name="login"),  # /login/
    path('customer/<int:id>/', views.load_customer, name="customer"),  # /login/customer/1/
    path('waiter/<int:id>/', views.load_waiter),  # /login/waiter/1/
    path('chef/<int:id>/', views.load_chef),  # /login/chef/1/
    path('update-stock/<int:item_id>/<int:id>/<str:operation>/', views.update_stock, name='update_stock'),
    path('update-order/<int:order_number>/<int:id>/<str:operation>/', views.update_order, name='update_order'),
    path('update-order-waiter/<int:order_number>/<int:id>/<str:operation>/', views.update_order_waiter, name='update_order_waiter'),
]

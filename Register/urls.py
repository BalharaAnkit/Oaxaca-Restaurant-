from django.urls import path
from . import views

urlpatterns = [
    path('Register/', views.load_register, name="register"),
]

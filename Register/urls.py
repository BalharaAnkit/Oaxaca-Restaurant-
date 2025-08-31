from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_register, name="register"),   # http://127.0.0.1:8000/Register/
]

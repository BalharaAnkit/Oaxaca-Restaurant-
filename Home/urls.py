from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_home, name="home"),   # http://127.0.0.1:8000/Home/
    path('Menu/', views.load_menu, name="menu"),
    path('About/', views.load_about, name="about"),
    path('Contact/', views.load_contact, name="contact"),
    path('Make-Order/', views.process_order, name='process-order'),
    path('booking.html', views.load_booking, name='booking'),
    path('subscribe/', views.subscribe, name='subscribe'),
]

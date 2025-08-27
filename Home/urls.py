from django.urls import path
from . import views

urlpatterns = [
    path('Home/', views.load_home, name="home"),
    path('Menu/', views.load_menu, name="menu"),
    path('About/', views.load_about, name="about"),
    path('Contact/', views.load_contact, name="contact"),
    path('Make-Order/', views.process_order, name='process-order'),
    path('Home/booking.html', views.load_booking, name='booking'),
    path('subscribe/', views.subscribe, name='subscribe'),

]


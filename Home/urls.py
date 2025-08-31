from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_home, name="home"),  # /home/
    path('menu/', views.load_menu, name="menu"),  # /home/menu/
    path('about/', views.load_about, name="about"),  # /home/about/
    path('contact/', views.load_contact, name="contact"),  # /home/contact/
    path('make-order/', views.process_order, name='process-order'),  # /home/make-order/
    path('booking/', views.load_booking, name='booking'),  # /home/booking/
    path('subscribe/', views.subscribe, name='subscribe'),  # /home/subscribe/
]

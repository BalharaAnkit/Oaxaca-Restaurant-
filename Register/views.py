from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from Backend.models import Users, Customers, Waiters, KitchenStaff
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.
def load_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        role = request.POST.get('role')

        if password == password2:
            if Users.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                new_user = Users(username=username, email=email, password=make_password(password), role=role)
                new_user.save()
                if role == "CUST":
                    new_customer = Customers(user=new_user)
                    new_customer.save()
                elif role == "WAIT":
                    new_waiter = Waiters(user=new_user)
                    new_waiter.save()
                else:
                    new_chef = KitchenStaff(user=new_user)
                    new_chef.save()

                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'register.html')
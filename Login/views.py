from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from Backend.models import Users
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from Backend.models import Orders, MenuItem, Tables
from django.shortcuts import get_object_or_404
from collections import Counter
# Create your views here.
def load_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        try:
            user = Users.objects.filter(username=username, role=role).first()
            if check_password(password, user.password):
                return redirect(f"{Users.CHOICES.get(role)}/{user.user_id}")
            else:
                messages.error(request, 'Password is incorrect.')
        except:
            messages.error(request, 'Username/Role is incorrect.')

    return render(request, 'login.html')


def load_customer(request, id: int):
    temp = id
    menu_items = MenuItem.objects.all().values()
    tables = Tables.objects.all()
    username = Users.objects.values('user_id', 'username')
    username = {user['user_id']: user['username'] for user in username}
    username = username.get(id)
    allergen_filter = request.GET.get('allergen') 
    orders = Orders.objects.filter(status='P')
    unavailable_table_ids = {order.table_id for order in orders}
    
    if allergen_filter:
        menu_items = menu_items.filter(allergies__contains=allergen_filter)


    tables_list = []
    for table in tables:
        table_info = {
            'table_id': table.table_id,  
            'size': table.capacity,  
            'location': table.location,
            'unavailable': table.table_id in unavailable_table_ids  
        }
        tables_list.append(table_info)
    template = loader.get_template('customer.html')
    context = {
        'menu_item': menu_items,
        'tables': tables_list,
        'orders': orders,
        'user': username,
        'userid': id
    }
    return HttpResponse(template.render(context, request))


def load_waiter(request, id: int):
    temp = id
    orders = Orders.objects.all()
    for order in orders:
        order.items_list = order.items.split(',')
        item_counts = Counter(item.strip() for item in order.items_list)
        order.item_quantities = item_counts.items()
        if order.status == "P":
            order.detailed_status = "Pending"
        if order.status == "R":
            order.detailed_status = "Done"
        if order.status == "C":
            order.detailed_status = "Cancelled"
        if order.status == "D":
            order.detailed_status = "Delivered"

    username = Users.objects.values('user_id', 'username')
    username = {user['user_id']: user['username'] for user in username}
    username = username.get(id)
    template = loader.get_template('waiter.html')
    context = {

        'orders': orders,
        'user': username,
        'userid': id
    }
    return HttpResponse(template.render(context, request))

def load_chef(request, id: int):
    temp = id
    menu_items = MenuItem.objects.all().values()
    orders = Orders.objects.all()
    for order in orders:
        order.items_list = order.items.split(',')
        item_counts = Counter(item.strip() for item in order.items_list)
        order.item_quantities = item_counts.items()
        if order.status == "P":
            order.detailed_status = "Pending"
        if order.status == "R":
            order.detailed_status = "Done"
        if order.status == "C":
            order.detailed_status = "Cancelled"
        if order.status == "D":
            order.detailed_status = "Delivered"

    username = Users.objects.values('user_id', 'username')
    username = {user['user_id']: user['username'] for user in username}
    username = username.get(id)
    template = loader.get_template('chef.html')
    context = {
        'menu_item': menu_items,
        'orders': orders,
        'user': username,
        'userid': id
    }
    return HttpResponse(template.render(context, request))

def update_stock(request, item_id, id, operation):
    item = get_object_or_404(MenuItem, pk=item_id)

    if operation == 'increase':
        item.stock += 1
    elif operation == 'decrease':
        item.stock = max(item.stock - 1, 0)

    item.save()


    return redirect(f'/Login/Chef/{id}/#menu')

def update_order(request, order_number,id, operation):
    item = get_object_or_404(Orders, pk=order_number)
    item.status = operation

    item.save()

    chef_id = request.session.get('chef_id') or 1  # Replace with appropriate logic to get the chef's id
    menu_items = MenuItem.objects.all().values()
    orders = Orders.objects.all().values()
    template = loader.get_template('chef.html')
    context = {
        'menu_item': menu_items,
        'orders': orders
    }
    return redirect(f'/Login/Chef/{id}/#orders')

def update_order_waiter(request, order_number,id, operation):
    item = get_object_or_404(Orders, pk=order_number)
    item.status = operation

    item.save()

    chef_id = request.session.get('chef_id') or 1  # Replace with appropriate logic to get the chef's id
    menu_items = MenuItem.objects.all().values()
    orders = Orders.objects.all().values()
    template = loader.get_template('chef.html')
    context = {
        'menu_item': menu_items,
        'orders': orders
    }
    return redirect(f'/Login/Waiter/{id}/#orders')
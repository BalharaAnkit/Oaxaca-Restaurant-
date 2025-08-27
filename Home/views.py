from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader
from Backend.models import Orders, Tables, MenuItem
from datetime import datetime, timedelta
from .forms import SubscriberForm


# Create your views here.
@csrf_exempt
def load_home(request):
    response = render(request, 'index.html')

    if not request.COOKIES.get('welcome_shown'):
        expires = datetime.utcnow() + timedelta(minutes=3) 
        response.set_cookie('welcome_shown', 'true', expires=expires)

    return response


def load_menu(request):
    menu_items = MenuItem.objects.all().values()
    tables = Tables.objects.all()
    allergen_filter = request.GET.get('allergen') 
    orders = Orders.objects.filter(status='P')
    unavailable_table_ids = {order.table_id for order in orders}
    
    if allergen_filter:
        menu_items = menu_items.filter(allergies__contains=allergen_filter)


    tables_list = []
    for table in tables:
        table_info = {
            'table_id': table.table_id,  # or table.table_id if your model uses table_id
            'size': table.capacity,  # Assuming you have a size attribute
            'location': table.location,
            'unavailable': table.table_id in unavailable_table_ids  # Add unavailable attribute
        }
        tables_list.append(table_info)
    template = loader.get_template('menu.html')
    context = {
        'menu_item': menu_items,
        'tables': tables_list,
        'orders': orders
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def load_about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

@csrf_exempt
def load_contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

@csrf_exempt
def load_booking(request):
    template = loader.get_template('booking.html')
    return HttpResponse(template.render())

@csrf_exempt
def process_order(request):
    if request.method == 'POST':
        items = request.POST.get('items')
        total = request.POST.get('total')
        orderNumber = request.POST.get('orderNumber')
        tableNo = int(request.POST.get('tableNo'))

        # Create a new patient entry in the database using the Patient model

        try:
            table = Tables.objects.filter(table_id=tableNo).first()

            order = Orders(order_number=orderNumber, items=items, total_price=total, table=table)
            order.save()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            # Return an HTML response that includes a script for the JS alert
            return HttpResponse("""
            <html>
                <body>
                    <script>alert('Thank you for subscribing!');
                    window.location.href='/Home';</script>
                </body>
            </html>
            """)
        else:
            # Handle the case where the form is not valid
            return HttpResponse("""
            <html>
                <body>
                    <script>alert('Failed to subscribe. Please try again.'); history.go(-1);</script>
                </body>
            </html>
            """)
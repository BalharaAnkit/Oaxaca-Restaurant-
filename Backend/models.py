from django.db import models


class MenuItem(models.Model):
    # Defined fields to represent database columns
    item_id = models.IntegerField(primary_key=True) # Primary key column
    name = models.CharField(max_length=255)
    image = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    calories = models.IntegerField()
    allergies = models.TextField()
    category = models.CharField(max_length=255)
    stock = models.IntegerField()


class Users(models.Model):
    CUSTOMER = "CUST"
    WAITER = "WAIT"
    CHEF = "CHEF"

    CHOICES = {
        CUSTOMER: "Customer",
        WAITER: "Waiter",
        CHEF: "Chef",

    }

    user_id = models.AutoField(primary_key=True)  # Primary key column
    username = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    role = models.CharField(max_length=4, choices=CHOICES, default=CUSTOMER)


class Customers(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)  # One-to-one relationship with Users table
    preferences = models.TextField()
    allergies = models.TextField()


class Waiters(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)  # One-to-one relationship with Users table
    shift = models.TextField()


class KitchenStaff(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)  # One-to-one relationship with Users table
    shift = models.TextField()


class Tables(models.Model):
    table_id = models.AutoField(primary_key=True)  # Primary key column
    capacity = models.IntegerField()
    location = models.CharField(max_length=255)


class Orders(models.Model):
    PLACED = "P"
    READY = "R"
    CANCELLED = "C"
    DELIVERED = "D"

    CHOICES = {
        PLACED: "Order Placed.",
        READY: "Order Ready.",
        CANCELLED: "Order Cancelled.",
        DELIVERED: "Order Delivered.",
    }

    order_number = models.IntegerField(primary_key=True)  # Primary key column
    order_time = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=1, choices=CHOICES, default=PLACED)
    items = models.TextField(null=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)

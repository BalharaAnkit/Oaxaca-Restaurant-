from django.db import models
from .models import MenuItem, Users

# basket class
class Basket(models.Model):
    # find associated baskets for a user
    # deletes baskets when the user is removed
    user = models.ForeignKey(Users, related_name='baskets', on_delete=models.CASCADE)
    # timestamp for when the basket is created
    basket_created_at = models.DateTimeField(auto_now_add=True)

# single item in a basket
class BasketItem(models.Model):
    # references the a Basket
    basket = models.ForeignKey(Basket, related_name='items', on_delete=models.CASCADE)
    # references the MenuItems
    menu_item = models.ForeignKey(MenuItem, related_name='basket_item', on_delete=models.CASCADE)
    # stores number of items in the basket
    # basket is created with 0 items
    quantity = models.PositiveIntegerField(default=0)

    def total_price(self):
        # set default total cost to 0
        total = 0
        # iterates through all items and uses the Price from the db
        for item in self.basket.items.all():
            total += item.menu_item.price
        return total
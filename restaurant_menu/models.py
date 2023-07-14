from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes","Main Dishes"),
    ("desserts", "Desserts")
) # Each "sub-tuple" has two items, one for the "backend name" and another one for the "Display Name"

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE) # Pre-set amount of choices instead of free text
    author = models.ForeignKey(User, on_delete = models.PROTECT) # Importing class (see above) which represents a "User Database Model" (table in the DB)
                                     # We establish a relationship between DB objects like this 
                                     # It is a "many-to-one relationship": one "author" can create many "Items (meals)"
                                     # When a User is deleted:
                                     # on_delete = models.CASCADE deletes all his created meals
                                     # on_delete = models.PROTECT doesn't delete all his created meals
                                     # on_delete = models.SET_NULL doesn't delete all his created meals and sets the "author" to NULL
    status = models.IntegerField(choices=STATUS, default = 1) # to make the meal available or not (by default available)
    date_created = models.DateTimeField(auto_now_add=True) # When a new "Item" is created, the timestamp will be recorded
    date_updated = models.DateTimeField(auto_now=True) # When an "Item" is edited, the timestamp will be recorded (overwritten)
    
    # The method below will print out the Item in the admin interface by its "meal" value
    def __str__(self):
        return self.meal






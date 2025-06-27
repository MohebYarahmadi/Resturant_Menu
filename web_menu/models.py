from django.db import models
from django.contrib.auth.models import User

# Tuple of Tuples for choices on meal_type
MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts")
)
# Tuple of Tuples for choices on status
STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

# Create model to define Item table in database - 55-04
class Items(models.Model):
    # Define each column for Items table
    meal = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=255, choices=MEAL_TYPE)  # Choices based on tuple
    status = models.IntegerField(choices=STATUS, default=1) # Another choices
    date_created = models.DateTimeField(auto_now_add=True)  # Creation time
    date_updated = models.DateTimeField(auto_now=True)  # Whenever Edited

    # Create a realtionship with User table
    # Many Items to One User - Manay to One
    # on_delete: when user deleted, what happens for it's relations
    # options for on_delete:
    #   CASCADE: Deteling User will delete all it's items
    #   PROTECT: You are not be able to delete User and Item
    #   SET_NULL: You can delete User and this col will set to null
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.meal

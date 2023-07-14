from django.shortcuts import render
from django.views import generic
from .models import Item

# Views can be "function-based" or "class-based" (like this one)
# In these classes, the variable names need to have these specific names
class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")  # querying data from DB table
    template_name = "index.html"  # instead of the "return" instruction of the function-based views

    def get_context_data(self):
        context = {"meals":"Pizza", # the key is the variable that can be accessed through the html template and the value is what is displayed in the UI
                   "ingredients":["tomato", "mozzarela"]}
        return context

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
from django.urls import path
from . import views # . is current directory

# connecting URLs with Views
urlpatterns = [
    path("", views.MenuList.as_view(), name="home"), # with function-based views we do not need the as_view method
    path("item/<int:pk>/", views.MenuItemDetail.as_view(), name="menu_item")
    # <int:pk> makes the link dynamic. A "primary key" from the Database is expected
]
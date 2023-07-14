from django.urls import path
from . import views # . is current directory

# connecting URLs with Views
urlpatterns = [
    path("", views.MenuList.as_view(), name="home"), # with function-based views we do not need the as_view method
    
]
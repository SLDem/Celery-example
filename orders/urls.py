from django.urls import path

from .views import *

urlpatterns = [
    path("orders/", view=OrdersView.as_view(), name="orders"),
    path("delete_order/<int:pk>", view=DeleteOrder.as_view(), name="delete_order")
]

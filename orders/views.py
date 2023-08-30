from django.views.generic import DeleteView, ListView
from django.urls import reverse_lazy

from .models import Order


class OrdersView(ListView):
    """
    Show a table with active orders.
    """
    model = Order
    template_name = 'orders/orders.html'

    def get_context_data(self, *args, **kwargs):
        context = {}
        employee = self.request.user
        orders = Order.objects.filter(employee=employee)
        context['employee'] = employee
        context['orders'] = orders
        return context


class DeleteOrder(DeleteView):
    """
    Delete order and redirect to main orders page.
    """
    model = Order
    success_url = reverse_lazy("orders")

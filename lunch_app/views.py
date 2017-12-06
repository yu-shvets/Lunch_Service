from django.views.generic.list import ListView
from .models import Order
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
import datetime


class OrderListView(ListView):

    model = Order
    template_name = 'index.html'

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(datetime__date=datetime.date.today())

    def get_context_data(self, **kwargs):
        total = []
        context = super(OrderListView, self).get_context_data(**kwargs)
        orders = Order.objects.filter(datetime__date=datetime.date.today())
        for order in orders:
            total.append(order.calculate_total())
        context['total'] = total
        context['day_total'] = sum(total)
        return context


class OrderUpdateView(UpdateView):
    model = Order
    fields = ['items']
    template_name = 'order_update_form.html'
    success_url = reverse_lazy('home')




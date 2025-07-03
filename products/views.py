from django.views import View
from django.shortcuts import redirect, get_object_or_404
from .models import Product, Order, OrderItem, Customer
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from django.http import Http404
from django.http import JsonResponse



class HomePageView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = list(Product.objects.all())
        random.shuffle(queryset)
        return queryset



class ProductSearchView(ListView):
    model = Product
    template_name = 'search_results.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(name__icontains=query)
        return Product.objects.none()

#Cart functionality
class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        

        try:
            customer = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            raise Http404("Customer profile not found.")

        # Get or create an incomplete order for the customer
        order, _ = Order.objects.get_or_create(customer=customer, complete=False)

        # Get or create order item
        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

        if not created:
            order_item.quantity += 1
            order_item.save()

        return redirect('home')  # or redirect back to product list
    


class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = Customer.objects.get(user=self.request.user)
        order = Order.objects.filter(customer=customer, complete=False).first()
        context['order'] = order
        context['items'] = order.items.all() if order else []
        return context


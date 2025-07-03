from django.urls import path
from . views import HomePageView, ProductSearchView, AddToCartView, CartView, TemplateView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', ProductSearchView.as_view(), name='product-search'),
    path('cart/', CartView.as_view(), name='view-cart'),
    path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add-to-cart'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('services/', TemplateView.as_view(template_name='services.html'), name='services'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
   
]

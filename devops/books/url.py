from django.urls import path
from books.views import getHomePage , contact , about , get_product_info , delete_product
urlpatterns = [
    path('home', getHomePage, name='homepage'),
    path('contact', contact , name='contact'),
    path('about', about , name='about'),
    path("products/<id>" , get_product_info , name='products.show'),
    path("products/<id>/delete" , delete_product , name='products.delete'),
]

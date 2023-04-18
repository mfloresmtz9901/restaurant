from django.urls import path

from .views import showproducts

urlpatterns = [
    path("product_list/", showproducts, name='products'),
]

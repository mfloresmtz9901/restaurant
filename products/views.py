from django.views.generic import TemplateView
from .models import Product

# Create your views here.


class HomeView(TemplateView):
    template_name = "products/home.html"


home_view = HomeView.as_view()

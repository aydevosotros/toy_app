from django.urls import path

from .views import hello_world
from .views import random_view
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', hello_world),
    path('cached/', cache_page(60 * 15)(random_view)),
]
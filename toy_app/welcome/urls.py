from django.urls import path
from django.views.decorators.cache import cache_page

from .views import hello_world
from .views import random_view
from .views import new_view

urlpatterns = [
    path('', hello_world),
    path('cached/', cache_page(60 * 15)(random_view)),
    path('new/', new_view),
]

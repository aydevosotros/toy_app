from random import randint

from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from .models import Visit


@api_view()
def hello_world(request):
    client_ip = get_client_ip(request)
    visit = Visit.objects.filter(ip=client_ip).first()
    if visit is None:
        visit = Visit(
            ip=client_ip,
            last_visit=datetime.now(),
            visits=0
        )
    visit.visits += 1
    visit.save()
    return Response(
        {"message": f"Hello, you. You have been here "
                    f"{visit.visits} times!"}
    )


@api_view()
def random_view(request):
    return Response(
        {'message': f'Returning from cached a cached number:'
                    f' {randint(0, 100)}!'}
    )


@api_view
def new_view(requests):
    return Response(
        {
            'message': f'Work In Progress. And keep going.'
        }
    )


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

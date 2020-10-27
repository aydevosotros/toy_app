import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toy_app.settings')

app = Celery()
app.config_from_object('django.conf:settings')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)


@app.task
def test(arg):
    print(arg)

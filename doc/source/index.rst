.. Toy! documentation master file, created by
   sphinx-quickstart on Fri Oct 30 14:45:47 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Toy!'s documentation!
================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Overview
========

What is this?
-------------

This project aims to be an educational project and provides a basic
implementation/configuration of a django based project that provides:

* Persistence by using a MySQL database
* Redis based cache
* Celery-beat set-up with RabbitMQ as broker.

More over, it has a docker-compose infrastructure set-up for local development
and unit/integration tests.
For deployment, it also provides a helm based kubernetes set-up. It also provides istio integration by
providing a virtual service and an istio gateway.




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

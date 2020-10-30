# The QToy project!

# Overview

## What is this?

This project aims to be an educational project and provides a basic
implementation/configuration of a django based project that provides:

* persistence by using a MySQL database
* Redis based cache
* celery-beat set-up with RabbitMQ as broker.

More over, it has a docker-compose infrastructure set-up for local development
and unit/integration tests. 
For deployment, it also provides a helm based kubernetes set-up. It also provides istio integration by
providing a virtual service and an istio gateway.

## What it is for?

This project pretends to be a based, easy to understand toy project
that allows you to understand and play with simple and easy blocks in 
a solid and robust infrastructure built on top of `kubernetes`, `helm`, `istio` and `fleet`.

# Get started


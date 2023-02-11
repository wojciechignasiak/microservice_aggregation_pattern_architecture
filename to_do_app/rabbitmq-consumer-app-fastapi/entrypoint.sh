#!/bin/sh

echo "Waiting for Postgres..."

while ! nc -z postgres 5432; do
  sleep 0.1
done

echo "Postgres started!"

while ! nc -z rabbitmq3 5672; do
  sleep 0.1
done
sleep 3

echo "RabbitMQ started!"

exec "$@"
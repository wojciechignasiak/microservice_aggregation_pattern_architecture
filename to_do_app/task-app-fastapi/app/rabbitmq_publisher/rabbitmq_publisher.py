import pika
import os

rabbitmq_username = os.environ.get("RABBITMQ_USER")
rabbitmq_password = os.environ.get("RABBITMQ_PASSWORD")

async def rabbitmq_publisher(operation: str, id: str):
    credentials = pika.PlainCredentials(rabbitmq_username,rabbitmq_password)
    parameters = pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    queue = 'aggregation_queue'
    channel.queue_declare(queue=queue, durable=True)

    message = operation + "/" + id
    channel.basic_publish(
        exchange='',
        routing_key=queue,
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )

    print(f"Sent message: {message}")

    connection.close()

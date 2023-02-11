import pika
from app.crud_operations.create_user import create_user
from app.crud_operations.delete_user import delete_user
from app.crud_operations.create_task import create_task
from app.crud_operations.delete_task import delete_task
import os

rabbitmq_username = os.environ.get("RABBITMQ_USER")
rabbitmq_password = os.environ.get("RABBITMQ_PASSWORD")

def rabbitmq_consumer(loop):
    credentials = pika.PlainCredentials(rabbitmq_username,rabbitmq_password)
    parameters = pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='aggregation_queue', durable=True)
    print("Waitnig for messages...")

    def decode_message_body(message_body):
        print(f"Decoding message {message_body}")
        decoded_body = message_body.split("/")
        print(decoded_body)

        if decoded_body[0] == "create_user":
            response = create_user(decoded_body[1])
            print(response)
            return response
        elif decoded_body[0] == "delete_user":
            response = delete_user(decoded_body[1])
            return response
        elif decoded_body[0] == "create_task":
            response = create_task(decoded_body[1])
            return response
        elif decoded_body[0] == "delete_task":
            response = delete_task(decoded_body[1])
            return response
        else:
            return True

    def acknowledgement_callback(ch, method, properties, body):
        print(f"Recived message: {body.decode()}")
        response = decode_message_body(body.decode())

        if response == True:
            ch.basic_ack(delivery_tag=method.delivery_tag)
        if response == False:
            ch.basic_nack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='aggregation_queue', on_message_callback=acknowledgement_callback)

    channel.start_consuming()
import pika
import json

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Received message: {message}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='file_notifications')

channel.basic_consume(queue='file_notifications', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='file_uploads')

def callback(ch, method, properties, body):
    print(f"Notification received: {body.decode()}")
    # Logic to sync the file across other devices

channel.basic_consume(queue='file_uploads', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

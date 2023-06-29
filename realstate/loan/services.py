import pika
import json
from django.conf import settings
import socket

class LogUtils:

    def __init__(self,host,port,username,password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def send_message_log(self,json_message,queue):

        credentials = pika.PlainCredentials(self.username,self.password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            self.host, self.port,'/',credentials))

        channel = connection.channel()
        channel.queue_declare(queue=queue,durable=True)
        channel.basic_publish(exchange='', routing_key=queue, body=json.dumps(json_message))

        connection.close()


class LogService:

    @staticmethod
    def send_log(json):

        log_utils = LogUtils(
            settings.RABBIT_HOST,settings.RABBIT_PORT,
            settings.RABBIT_USERNAME,settings.RABBIT_PASSWORD)

        log_utils.send_message_log(json
                             ,settings.RABBIT_LOG_QUEUE)

class IpService:

    @staticmethod
    def get_my_ip():
        hostname = socket.gethostname()
        endereco_ip = socket.gethostbyname(hostname)
        return endereco_ip



















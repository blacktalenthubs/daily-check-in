import json
import requests

from kafka import KafkaProducer

# Initialize a Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

def fetch_data(api_url):
    response = requests.get(api_url)
    return response.json()

def send_to_kafka(topic, data):
    producer.send(topic, value=data)
    producer.flush()

def main():
    # Example API URL
    api_url = "https://api.example.com/data"
    data = fetch_data(api_url)

    # Send data to three different topics
    send_to_kafka('input-topic-1', data)
    send_to_kafka('input-topic-2', data)
    send_to_kafka('input-topic-3', data)

if __name__ == '__main__':
    main()
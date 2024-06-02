from kafka import KafkaConsumer
import json

def consume_messages(topic_name):
    # Create a Kafka consumer
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',  # Start reading at the earliest message
        group_id='my-group')           # Consumer group ID

    # Print messages as they are consumed
    for message in consumer:
        msg = json.loads(message.value.decode('utf-8'))
        print(f"Received message on {topic_name}: {msg}")

if __name__ == "__main__":
    consume_messages('ad_requests')
    consume_messages('ad_responses')
    consume_messages('ad_clicks')
from kafka import KafkaProducer
import random
import time
from inputs import *

# Initialize Kafka Producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: x.encode('utf-8'))


def produce_messages():
    while True:
        # Create instances of each class
        ad_request = AdRequest()
        ad_response = AdResponse()
        ad_click = AdClick()

        # Populate fields (Example: randomly assign user_ids and timestamps)
        user_id = random.randint(1000, 9999)
        session_id = random.randint(100000, 999999)
        timestamp = int(time.time() * 1000)

        ad_request.user_id = user_id
        ad_request.session_id = session_id
        ad_request.timestamp = timestamp

        ad_response.user_id = user_id
        ad_response.session_id = session_id
        ad_response.timestamp = timestamp
        ad_response.request_id = ad_request.request_id  # Linking request and response

        ad_click.user_id = user_id
        ad_click.session_id = session_id
        ad_click.timestamp = timestamp
        ad_click.request_id = ad_request.request_id
        ad_click.response_id = ad_response.response_id  # Linking click to response

        # Serialize to JSON
        json_ad_request = ad_request.to_json()
        json_ad_response = ad_response.to_json()
        json_ad_click = ad_click.to_json()

        # Send to Kafka topics
        producer.send('ad_requests', json_ad_request)
        producer.send('ad_responses', json_ad_response)
        producer.send('ad_clicks', json_ad_click)

        # Wait before sending the next set of messages
        time.sleep(1)


if __name__ == '__main__':
    produce_messages()
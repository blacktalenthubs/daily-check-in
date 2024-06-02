from kafka import KafkaProducer, KafkaConsumer
from inputs import *
import pytest


class KafkaTestProducer:
    def __init__(self, topic, bootstrap_servers='localhost:9092'):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=[bootstrap_servers],
            value_serializer=lambda x: x.encode('utf-8')
        )

    def send_message(self, message):
        self.producer.send(self.topic, message)
        self.producer.flush()


def setup_test_data():
    # Create instances with test data
    ad_request = AdRequest(user_id=1234, session_id=5678)
    # Create producer and send data
    producer = KafkaTestProducer(topic='ad_requests')
    producer.send_message(ad_request.to_json())




@pytest.fixture(scope="module")
def kafka_reader():
    return KafkaObjectReader(topic='ad_requests', bootstrap_servers='localhost:9092', group_id='test_group')
def test_consume_messages(kafka_reader):
    setup_test_data()  # Make sure data is produced to Kafka before consuming
    messages = kafka_reader.consume_messages(max_messages=1)
    assert len(messages) > 0, "No messages consumed"
    for message in messages:
        assert message.user_id == 1234, "user_id does not match"
        assert message.session_id == 5678, "session_id does not match"

def test_consume_latest_messages(kafka_reader):
    setup_test_data()  # Make sure data is produced to Kafka before consuming
    messages = kafka_reader.consume_latest_messages(max_messages=1)
    assert len(messages) > 0, "No messages consumed"
    for message in messages:
        assert message.user_id == 1234, "user_id does not match"
        assert message.session_id == 5678, "session_id does not match"
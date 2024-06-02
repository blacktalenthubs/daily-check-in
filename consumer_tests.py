
import jsonpickle
from kafka import KafkaConsumer

class KafkaObjectReader:
    def __init__(self, topic, bootstrap_servers='localhost:9092', group_id=None):
        self.topic = topic
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id=group_id,
            value_deserializer=lambda x: jsonpickle.decode(x.decode('utf-8'))
        )

    def consume_messages(self, max_messages=None):
        """
        Consume messages from the specified topic and deserialize them into objects.
        :param max_messages: Maximum number of messages to consume or None for infinite.
        :return: List of deserialized objects.
        """
        objects = []
        for message in self.consumer:
            objects.append(message.value)
            if max_messages and len(objects) >= max_messages:
                break
        return objects

    def consume_latest_messages(self, max_messages=None):
        """
        Consume only the latest messages published after the consumer starts.
        This method assumes that the consumer is set to read from the latest offset.
        :param max_messages: Maximum number of messages to consume or None for infinite.
        :return: List of deserialized objects.
        """
        # Adjust consumer to start from the latest messages
        self.consumer.config['auto_offset_reset'] = 'latest'

        # This is a transient consumer specifically for latest messages
        latest_consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.consumer.config['bootstrap_servers'],
            auto_offset_reset='latest',
            enable_auto_commit=True,
            group_id=self.consumer.config['group_id'],
            value_deserializer=self.consumer.config['value_deserializer']
        )

        objects = []
        for message in latest_consumer:
            objects.append(message.value)
            if max_messages and len(objects) >= max_messages:
                break
        latest_consumer.close()  # Close the consumer when done
        return objects
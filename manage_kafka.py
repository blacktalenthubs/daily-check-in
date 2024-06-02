from kafka.admin import KafkaAdminClient, NewTopic

def create_topic(admin_client, topic_name, num_partitions, replication_factor):
    topic = NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)
    try:
        admin_client.create_topics(new_topics=[topic], validate_only=False)
        print(f"Topic '{topic_name}' created successfully.")
    except Exception as e:
        print(f"Failed to create topic '{topic_name}'. Error: {e}")

def main():
    # Configuration for connecting to Kafka
    admin_client = KafkaAdminClient(
        bootstrap_servers="localhost:9092",  # Adjust this if your Kafka server is on a different host
        client_id='create_topics_script'
    )

    topics = [
        ("ad_requests", 1, 1),
        ("ad_responses", 1, 1),
        ("ad_clicks", 1, 1),
       # ("nKeyword", 1, 1)
    ]

    for topic_name, partitions, replication in topics:
        create_topic(admin_client, topic_name, partitions, replication)

if __name__ == "__main__":
    main()
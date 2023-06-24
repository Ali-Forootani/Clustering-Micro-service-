from kafka import KafkaProducer


def publish_message(producer_instance, topic_name, key):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer


if __name__ == '__main__':
    kafka_producer = connect_kafka_producer()
    publish_message(kafka_producer, "clustering_request", '1ab2')
    publish_message(kafka_producer, "clustering_request", '2ab3')
    #publish_message(kafka_producer, "clustering_request", '5ab6')
    # publish_message(kafka_producer, "my_topic", '7ab8')
    # publish_message(kafka_producer, "my_topic", '9ab10')


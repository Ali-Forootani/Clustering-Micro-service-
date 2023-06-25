# Clustering-Micro-service

I developed a Micro service for the task of clustering trucks or delivery vehices based on their x-y coordinate and the time.

It is based on Kafka message broker, Redis data base and Python.
I have to add many explanation so that a user could digest what was in my mind when I formulate and wrote such things.

I added these explanations here so you can take a look.

# Kafka Message Publisher (dummy producer)

This script allows you to publish messages to a Kafka topic using the `kafka-python` library.

## Prerequisites

- Python 3.x
- `kafka-python` library

## Installation

1. Make sure you have Python 3.x installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. Install the `kafka-python` library using pip:

   ```
   pip install kafka-python
   ```

3. Ensure you have a running Kafka broker. You can follow the Kafka documentation to set up Kafka locally: https://kafka.apache.org/quickstart

## Usage

1. Open the `kafka_publisher.py` file in a text editor.

2. Modify the following line to set the appropriate bootstrap server for your Kafka broker:

   ```python
   _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
   ```

   Replace `localhost:9092` with the hostname and port of your Kafka broker.

3. Optionally, uncomment the `publish_message` calls and modify them as needed to publish messages to different topics:

   ```python
   publish_message(kafka_producer, "clustering_request", '1ab2')
   publish_message(kafka_producer, "clustering_request", '2ab3')
   # publish_message(kafka_producer, "clustering_request", '5ab6')
   # publish_message(kafka_producer, "my_topic", '7ab8')
   # publish_message(kafka_producer, "my_topic", '9ab10')
   ```

   - The first argument is the Kafka producer instance.
   - The second argument is the topic name.
   - The third argument is the message key.

   Customize these values according to your requirements.

4. Save the file.

5. Open a terminal or command prompt and navigate to the directory where the `kafka_publisher.py` file is located.

6. Run the script using the following command:

   ```
   python kafka_publisher.py
   ```

   The script will connect to the Kafka broker, publish the specified messages to the specified topics, and print a success message for each published message.

That's it! You have successfully used the Kafka Message Publisher script to publish messages to a Kafka topic.

Feel free to modify the code according to your specific needs and extend it further if required.

Note: Make sure your Kafka broker is running and the specified topics exist before executing the script.

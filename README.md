# Clustering-Micro-service

I developed a Micro service for the task of clustering trucks or delivery vehices based on their x-y coordinate and the time.

It is based on Kafka message broker, Redis data base and Python.
I have to add many explanation so that a user could digest what was in my mind when I formulate and wrote such things.

I added these explanations here so you can take a look.

# Kafka Message Publisher (dummy_producer.py)

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


Certainly! Here's a README file that provides an overview of the code and instructions for using it:

# Kafka Consumer Clustering Service (cosumer.py)

This script utilizes the Faust library to consume messages from a Kafka topic, retrieve input data from Redis, and perform clustering on the received data.

## Prerequisites

- Python 3.x
- `faust` library
- `redis` library
- Kafka broker
- Redis server

## Installation

1. Make sure you have Python 3.x installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. Install the required libraries using pip:

   ```
   pip install faust redis
   ```

3. Ensure you have a running Kafka broker. You can follow the Kafka documentation to set up Kafka locally: https://kafka.apache.org/quickstart

4. Set up a Redis server. You can download and install Redis from the official website: https://redis.io/download

## Usage

1. Open the `consumer_clustering_service.py` file in a text editor.

2. Modify the following variables at the beginning of the script to configure the Redis connection:

   ```python
   redis_host = 'localhost'
   redis_port = 6379
   ```

   Update `redis_host` and `redis_port` with the appropriate values according to your Redis server configuration.

3. Implement the `process_packet_list` function in the `clustering_module` module according to your clustering logic. Uncomment the following line in the script:

   ```python
   # from clustering_module import process_packet_list
   ```

   Ensure that the `process_packet_list` function is correctly defined in the `clustering_module.py` file.

4. Save the file.

5. Open a terminal or command prompt and navigate to the directory where the `consumer_clustering_service.py` file is located.

6. Run the Faust worker using the following command:

   ```
   faust -A consumer_clustering_service -l info worker --web-port=6069
   ```

   Replace `consumer_clustering_service` with the name of your Python file containing the Faust application.

   The Faust worker will start, connect to the Kafka broker, consume messages from the specified Kafka topic, retrieve the input data from Redis, and perform clustering on the received data.

7. Ensure that the Kafka topic `'clustering_request'` exists and contains messages to be consumed.

8. Verify the clustering results. The script currently prints the clustering ID labels obtained from the `process_packet_list` function. Modify the script as needed to store or further process the clustering results.

That's it! You have successfully set up and run the Kafka Consumer Clustering Service script.

Feel free to customize the code according to your specific requirements, including modifying the Redis connection details, implementing the clustering logic, and handling the clustering results.

Note: Ensure that your Kafka broker and Redis server are running and properly configured before executing the script.

Note: Make sure your Kafka broker is running and the specified topics exist before executing the script.


The provided code appears to be a Python script that imports several libraries and defines various functions for data processing and clustering. Here's a README file that explains the script and provides some information about its usage:

# Clustering Module (clustering_module.py)

This script is a clustering module that performs various clustering algorithms on input data. It includes functions for data preprocessing, time scheduling detection, time computation, and different clustering techniques.

## Prerequisites

The script requires the following libraries to be installed:

- redis
- json
- random
- decimal
- math
- numba
- pandas
- os
- glob
- sklearn
- nltk
- networkx
- kmeans1d
- seaborn
- matplotlib
- pickle
- kafka

You can install these libraries using pip, for example:

```
pip install redis jsonlib numba pandas scikit-learn nltk networkx seaborn matplotlib kafka-python
```

## Usage

To use the clustering module, follow these steps:

1. Import the necessary functions and modules from the script into your Python program. For example:

```python
from time_window_detection import time_window_seperation
from scheduling_module import time_scheduling_function
from time_computation_module import time_computation_function
from many_pickup_fixed_delivery_clustering_module import many_pickup_fixed_delivery_clustering_function
...
```

2. Establish a connection to a Redis server by providing the host and port information. For example:

```python
redis_host = 'localhost'
redis_port = 6379

r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
```

3. Define your input data in the JSON format. You can retrieve this data from the Redis server or any other data source. For example:

```python
packet_list = json.loads(r.get('1ab2'))
```

4. Call the `process_packet_list` function with the input data to perform clustering. For example:

```python
clustering_id_labels, ids = process_packet_list(packet_list)
```

5. The function will return the clustering results, including the cluster labels and IDs. You can then use or store these results as needed.

6. Repeat steps 3 to 5 for any additional input data.

Note: You may need to modify the code and functions to suit your specific use case and data format.

## Additional Information

- The script uses various clustering algorithms, such as K-means, Affinity Propagation, and Birch, depending on the specific function being called. You can find more information about these algorithms in the respective function files.

- The script also includes functions for estimating the maximum number of clusters based on the input data.

- Some functions require specific input data formats, such as time window information and geographical coordinates. Make sure to provide the data in the expected format for accurate clustering results.

- The script uses the Redis server for storing and retrieving data. You can modify the code to use a different data storage solution if desired.

- It is recommended to review and understand the code before using it, as well as consult the function files for more details on their implementation.

That's the README file for the clustering module script.




## Scheduling Module Unit Test

This repository contains a unit test script for the `time_scheduling_function` in the `scheduling_module`. The unit test script is written in Python using the `unittest` framework.

## Getting Started

To get started with the unit test, follow these steps:

1. Clone the repository to your local machine.
2. Ensure that you have Python installed on your machine.
3. Make sure the `scheduling_module` and its dependencies are in the same directory as the test script.

## Running the Unit Test

To run the unit test, execute the test script from the command line. The `unittest` framework will automatically discover and run the test cases defined within the script.

Run the following command to execute the test script:

```
python test_scheduling_module.py
```

Replace `test_scheduling_module.py` with the name of your test script file.

The framework will provide detailed information about the test results, including which tests passed and which ones failed, along with any error messages or exceptions raised during the test execution.

## Test Cases

The unit test script includes the following test cases:

- `test_Yearly`: Tests the scheduling function for yearly scheduling.
- `test_Monthly`: Tests the scheduling function for monthly scheduling.
- `test_Weekly`: Tests the scheduling function for weekly scheduling.
- `test_Daily`: Tests the scheduling function for daily scheduling.
- `test_wrong_input_data_2` to `test_wrong_input_data_9`: Tests for various incorrect input data formats.
- `test_negative_input_data_1` to `test_negative_input_data_8`: Tests for negative input data.

Each test case verifies a specific aspect of the scheduling function's behavior.

## Contributing

Contributions to this repository are welcome. If you find any issues or want to suggest improvements, please open an issue or submit a pull request.

## License

This repository is licensed under the [MIT License](LICENSE).
```


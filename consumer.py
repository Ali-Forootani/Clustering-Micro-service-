import faust
import redis
import json


#from clustering_module import reading_input_data_consumer
from clustering_module import process_packet_list

# Syntax to run the faust worker
# faust -A consumer -l info worker --web-port=6069/6068/2028/etc.


app = faust.App('consumer_clustering_service', broker='kafka://localhost:9092')

topic_clustering_service = app.topic('clustering_request', key_type=bytes, partitions=1)


redis_host='localhost'
redis_port= 6379

r=redis.StrictRedis(host=redis_host,port=redis_port,decode_responses=True)


@app.agent(topic_clustering_service)
async def clustering_request(stream):
    async for event_key, event_value in stream.items():
        print(f'we are doing clustering service: {event_key}')
        #r=redis.StrictRedis(host=redis_host,port=redis_port,decode_responses=True)
        input_data=json.loads(r.get(event_key))
        print("--------")
        #print(input_data)
        print("--------")

        clustering_id_labels = process_packet_list(input_data)

        print(clustering_id_labels)





if __name__ == '__main__':
    app.main()

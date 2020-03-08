from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import time


value_schema_str = """
{
   "namespace": "mddarr.kafkatweets",
   "name": "value",
   "type": "record",
   "fields" : [
     {"name" : "created_at", "type" : "int", "logicalType": "date"},
    {"name" : "username", "type" : "string"},
    {"name" : "location", "type" : "string"},
    {"name" : "text", "type" : "string"}    
   ]
}
"""

key_schema_str = """
{
   "namespace": "mddarr.kafkatweets",
   "name": "key",
   "type": "record",
   "fields" : [
     {"name" : "id", "type" : "int"}
   ]
}
"""

value_schema = avro.loads(value_schema_str)
key_schema = avro.loads(key_schema_str)
# value = {"location":"Seattle","created_at": int(time.time()),"text":"Bernie is a moron","username":"Trump train"}
# key = {"id": 1}
#
# avroProducer = AvroProducer({
#     'bootstrap.servers': 'localhost:9092',
#     'schema.registry.url': 'http://localhost:8081'
#     }, default_key_schema=key_schema, default_value_schema=value_schema)
#
# avroProducer.produce(topic='kafka_tweets', value=value, key=key)
# avroProducer.flush()

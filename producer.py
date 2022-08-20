from kafka import KafkaProducer
import logging
import json

logging.basicConfig(level=logging.INFO)

producer = KafkaProducer(
    bootstrap_servers="127.0.0.1:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

while True:
    message = input("type your message here:")
    producer.send("topic_test", {"message": message})
    producer.flush()

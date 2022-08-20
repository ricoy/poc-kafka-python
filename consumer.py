from kafka import KafkaConsumer
import logging

logging.basicConfig(level=logging.INFO)

consumer = KafkaConsumer("topic_test")
for msg in consumer:
    print(msg.value)

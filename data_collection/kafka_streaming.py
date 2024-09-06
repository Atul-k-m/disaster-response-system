from kafka import KafkaConsumer

def stream_data_from_kafka(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092')
    for message in consumer:
        process_message(message.value)

def process_message(message):
 
    print(f"Processing message: {message}")

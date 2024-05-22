# file_watcher.py
import json
from kafka import KafkaConsumer
import queue
import threading
from audit import main

class FileProcessor:
    def __init__(self):
        self.queue = queue.Queue()

    def start_worker(self):
        for _ in range(5):  # Number of worker threads
            t = threading.Thread(target=self.process_queue)
            t.daemon = True  # Daemon threads exit when the program does
            t.start()


    def process_queue(self):
        while True:
            dt = self.queue.get()  # Blocks until an item is available
            
            try:
                print('Received Audit Request')
                main()
            except Exception as e:
                print(f"Failed to process: {e}")
            finally:
                self.queue.task_done()  # Signals that the queue item's processing is complete


def consume_kafka_messages(topic, bootstrap_servers, processor):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers
    )
    print("Parser started")
    for message in consumer:
        try:
            parsedMsg = json.loads(message.value)
            processor.queue.put(parsedMsg)
        except Exception as e:
            print(f"Exception occurred when processing Kafka message: {e}")


if __name__ == "__main__":
    KAFKA_BOOTSTRAP_SERVER = '192.168.4.195:9092'
    KAFKA_TOPIC = 'test_gpl'
    processor = FileProcessor()
    processor.start_worker()  # Start worker threads
    consume_kafka_messages(KAFKA_TOPIC, KAFKA_BOOTSTRAP_SERVER, processor)
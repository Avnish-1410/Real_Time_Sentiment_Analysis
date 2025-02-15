from time import sleep
import csv 
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))

with open(r"C:\Users\avnis\OneDrive\Desktop\Real-Time-Twitter-Sentiment-Analysis-main\Kafka-PySpark\twitter_validation.csv", 'r', encoding='utf-8') as file_obj:
    reader_obj = csv.reader(file_obj)
    print("File opened successfully")
    for data in reader_obj: 
        print("Sending tweet:",data)
        producer.send('numtest', value=data)
        sleep(3)
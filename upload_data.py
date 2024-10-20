from pymongo.mongo_client import MongoClient 
import pandas as pd
import json 

# create database and collection 
DATABASE_NAME = "Sensor_Project"
COLLECTION_NAME = "data_list"
uri = "mongodb+srv://Sudhir-Nishad:OTAqbDiq1a3JvAWg@cluster0.ybyy5vm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
df = pd.read_csv("./notebook/wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1) 
json_record = list(json.loads(df.T.to_json()).values())
type(json_record)
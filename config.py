import pymongo
import certifi


con_str= "mongodb+srv://FSDICh29:RKZBhFPzYQAOUYrv@cluster0.g4ejq.mongodb.net/?retryWrites=true&w=majority"

client= pymongo.MongoClient(con_str,tlsCAFile=certifi.where())

db= client.get_database("Organix-Store")



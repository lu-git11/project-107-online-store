import pymongo
import certifi

con_str = 'mongodb+srv://test:test@cluster0.crhkdhh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database('Amazan_2')





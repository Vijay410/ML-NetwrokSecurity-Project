
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from urllib.parse import quote_plus

username = quote_plus("")
password = quote_plus("")
uri = f"mongodb+srv://{username}:{password}@cluster0.ylo83gs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&tls=true&tlsAllowInvalidCertificates=true"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
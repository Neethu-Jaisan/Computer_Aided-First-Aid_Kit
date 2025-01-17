import pymongo

# Replace with your actual connection details
MONGODB_URI = "mongodb+srv://fedauser:fedauser@fedacluster.aemzpay.mongodb.net/"
DATABASE_NAME = "fedadb"

client = pymongo.MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]

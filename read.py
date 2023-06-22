import pymongo
client = pymongo.MongoClient('mongodb+srv://Avi:123456789avi@cluster0.hfav1gq.mongodb.net/Avi')


db = client['mydb']
mycol = db ['employee']
for x in mycol.find():
print (x)
print ("All Data is Displyed")
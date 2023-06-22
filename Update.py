import pymongo
client = pymongo.MongoClient('mongodb+srv://Avi:123456789avi@cluster0.hfav1gq.mongodb.net/Avi')


db = client['mydb']
mycol = db ['employee']
myquary = {"name":"Abil Vargase","Address":"Nashik","id":36}
newvalues = {"$set":{"name":"Abil","Address":"Nashik","id":1}}
mycol.update_one(myquary, newvalues)
for x in mycol.find():
print (x)
print ("All Data is Updated")
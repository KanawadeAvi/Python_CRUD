import pymongo   # importing py mongo lib
client = pymongo.MongoClient('mongodb+srv://Avi:123456789avi@cluster0.hfav1gq.mongodb.net/Avi')    #conectivity of Database


db = client['mydb']  #Database Name
mycol = db ['employee']  #Table name
Mydict = {"name":"Avi","Address":"Sangamner","id":37}  #data to be inserted
x = mycol.insert_one(Mydict)   #making Objecct
print(x)
print ("Data is inserted")



# insert Many
'''import pymongo
client = pymongo.MongoClient('mongodb+srv://Avi:123456789avi@cluster0.hfav1gq.mongodb.net/Avi')


db = client['mydb']
mycol = db ['employee']
Mylist =[{"name":"Abil","Address":"Nashik","id":36},
         {"name":"Gaurav","Address":"Dubai Fata","id":39},
         {"name":"Datta","Address":"Latur","id":38}
         ] 
x = mycol.insert_many(Mylist)
print(x)
print ("Data is inserted")'''
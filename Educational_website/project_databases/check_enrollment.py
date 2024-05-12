import pymongo

course_id=""
username=""



con = pymongo.MongoClient("mongodb://localhost:27017")
mydb = con['all_users_table']
mytb= mydb[username]
x = mytb.find_one({'_id':course_id},{})
if x == None:
    pass
else:
    pass
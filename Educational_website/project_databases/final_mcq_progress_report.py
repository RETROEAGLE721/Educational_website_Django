import pymongo

_id = ""
course_name=""
col_name=""

con = pymongo.MongoClient('mongodb://localhost:27017')
mydb = con['Final_mcq_progerss']
mytb= mydb[course_name]
mytb.update_one({'_id':_id},{'$set':{'col_name':1}})

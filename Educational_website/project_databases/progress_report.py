from datetime import datetime 
import pymongo

course_name=""
course_id=""
col_name=""

con = pymongo.MongoClient("mongodb://localhost:27017")
mydb = con['courses_progress']
mytb = mydb[course_name]
mytb.update_one({'_id':course_id},{'$set':{col_name:1}})
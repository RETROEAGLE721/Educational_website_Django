import datetime 
import pymongo

con = pymongo.MongoClient("mongodb://127.0.0.1:27017")

_id = ""
course_name=""
course_code=""
username=""
email=""

mydb = con['courses']
mytb = mydb[course_name+'_course_completed']
mytb.insert_one({'_id':_id,'username':username,'email':email,'course_code':course_code ,'course_name':course_name,'Completion_time':datetime.datetime.now()})


mydb = con['all_users_table']
mytb = mydb[username]
mytb.update_one({'course_code':course_code},{'$set':{'completed':'1','completion_time':datetime.datetime.now()}})


mydb = con['courses']
mytb = mydb['all_courses']
x = mytb.find_one({'course_code':course_code},{})
a = 1 + int(x['total_users_completed'])
mytb.update_one({'course_code':course_code},{'$set':{'total_users_completed':str(a)}})


mydb = con['courses']
mytb = mydb[course_name]
mytb.delete_one({'_id':_id})




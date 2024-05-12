from datetime import datetime
import pymongo


_id = ""
course_name=""
course_id=""
username=""
email=""


con = pymongo.MongoClient("mongodb://localhost:270170")
mydb = con['courses']
mytb = mydb[course_name]
mytb.insert_one({'_id': _id,'username': username,'email': email,'Enrollment_time': datetime.datetime.now()})


mydb = con['courses_progress']
mytb = mydb[course_name]
data = {'_id':_id,'username':username,'email':email,'Introducation_Of_Java':0,'Operators':0,'Scanner':0,'Type_Casting':0,'if_else':0,'Loops':0,'Switch':0,'Class_and_Constructor':0,'This_Keyword':0,'Object_':0,'Anonymous_Object':0,'Method':0,'Access_Modifiers':0,'FinalClass':0,'Final_Variable':0,'Final_Method':0,'Method_Overriding':0,'Inheritance':0,'Single_Inheritance':0,'Muiltilevel_Inheritance':0,'Muiltiple_hybrid_Inheritance':0,'Hierarchical_Inheritance':0,'Super_Keyword':0,'Abstract_Class_And_Method':0,'Interface':0,'Exception_handling':0,'try_catch':0,'finally_Block':0}
mytb.insert_one(data)


mydb = con['courses']
mytb= mydb['all_courses']
x = mytb.find_one({'_id':course_id},{})
a = 1 + int(x['total_users_enrolled'])
mytb.update_one({'_id':course_id},{'$set':{'total_users_completed':str(a)}})


mydb = con['all_users_table']
mytb = mydb[username]
mytb.insert_one({'_id':course_id,'course_name':course_name,'completed':'0','Enrollment_time':datetime.datetime.now(),'completion_time':"0"})


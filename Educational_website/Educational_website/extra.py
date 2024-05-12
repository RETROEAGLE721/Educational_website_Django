import pymongo
import datetime

con = pymongo.MongoClient("mongodb://localhost:27017")
mydb = con['courses']
mytb = mydb['all_courses']
mytb.insert_one({"_id":101,"course_name":'java','Total_topics':28,"total_users_enrolled":0,"total_users_completed":0,'courses_launch_date':datetime.datetime.now().isoformat()})
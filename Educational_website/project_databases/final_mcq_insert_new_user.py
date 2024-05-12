from datetime import datetime
import pymongo

_id = ""
course_name=""
username=""
email=""

con = pymongo.MongoClient("mongodb://localhost:27017")
mydb = con['Final_mcq_progerss']
mytb= mydb[course_name]
mytb.insert_one({'_id':_id,'username':username,'email':email,'-1-':0,'-2-':0,'-3-':0,'-4-':0,'-5-':0,'-6-':0,'-7-':0,'-8-':0,'-9-':0,'-10-':0,'-11-':0,'-12-':0,'-13-':0,'-14-':0,'-15-':0,'-16-':0,'-17-':0,'-18-':0,'-19-':0,'-20-':0,'-21-':0,'-21-':0,'-22-':0,'-23-':0,'-22-':0,'-23-':0,'-24-':0,'-25-':0,'-26-':0,'-27-':0,'-28-':0,'-29-':0,'-30-':0})

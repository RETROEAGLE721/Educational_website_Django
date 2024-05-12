import pymongo

course_name=""
course_id=""
col_name=""

con = pymongo.MongoClient("mongodb://localhost:27017")
mydb = con['courses_progress']
mytb = mydb[course_name]
x = mytb.aggregate(
    [
        {
            "$group": {
                "total_attained":{"$sum":["-1-","-2-","-3-","-4-","-5-","-6-","-7-","-8-","-9-","-10-","-11-","-12-","-13-","-14-","-15-","-16-","-17-","-18-","-19-","-20-","-21-","-22-","-23-","-24-","-25-","-26-","-27-","-28-","-29-","-30-"]}
            }
        }
    ]
)
if x['total_amount'] == 30:
    pass
import pymongo
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def view_website_all_users(request):
    con = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = con["total_users_of_website"]
    mytb=mydb["user_details_of_website"]
    data="""<html lang="en">
            <head>
                <title>All data</title>
            </head>
            <style>
                table,tr,td,th {
                    border: 2px solid black;
                    border-collapse: collapse;
                    padding: 5px;
                    color : white;
                }   
                body{
                    height: auto !important;
                    overflow-y:scroll ; 
                    overflow-x: hidden;
                    color: white !important;
                    background-color: #000213;
                    font-family: 'Times New Roman', Times, serif;
                }
                
                ::-webkit-scrollbar {
                    width: 10px;
                }
                
                ::-webkit-scrollbar-track {
                    background: none; 
                }
                
                ::-webkit-scrollbar-thumb {
                    background: #0046af; 
                }
                
                ::-webkit-scrollbar-thumb:hover {
                    background: #237bfffb; 
                }

                
                div::-webkit-scrollbar-track {
                    background: none; 
                }
                
                div::-webkit-scrollbar-thumb {
                    background: none; 
                }
                
                div::-webkit-scrollbar-thumb:hover {
                    background: none; 
                }
                table,th,td{
                    border : 5px solid red;
                }
                
                
            </style>
            <body>
                <table>
                    <tr>
                        <th>username</th>
                        <th>email</th>
                        <th>password</th>
                        <th>total_courses_enrolled</th>
                        <th>total_courses_completed</th>
                        <th>Registration_time</th>
                    </tr>"""
    data_2=""
    for x in mytb.find({},{}):
        data_2=data_2+"""<tr>
                    <td>"""+str(x['username'])+"""</td>
                    <td>"""+str(x['email'])+"""</td>
                    <td>"""+str(x['password'])+"""</td>
                    <td>"""+str(x['total_courses_enrolled'])+"""</td>
                    <td>"""+str(x['total_courses_completed'])+"""</td>
                    <td>"""+str(x['Registration_time'])+"""</td>
                </tr>
       """
    data = data+data_2
    data = data + """</table>
        </body>
        </html>"""
    return HttpResponse(data)



def all_enrolled_users(request):
    course = request.POST.get('enroll_users')
    con = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = con["courses"]
    mytb=mydb[course]
    data="""<html lang="en">
            <head>
                <title>All data</title>
            </head>
            <style>
                table,tr,td,th {
                    border: 2px solid black;
                    border-collapse: collapse;
                    padding: 5px;
                    color : white;
                }   
                body{
                    height: auto !important;
                    overflow-y:scroll ; 
                    overflow-x: hidden;
                    color: white !important;
                    background-color: #000213;
                    font-family: 'Times New Roman', Times, serif;
                }
                
                ::-webkit-scrollbar {
                    width: 10px;
                }
                
                ::-webkit-scrollbar-track {
                    background: none; 
                }
                
                ::-webkit-scrollbar-thumb {
                    background: #0046af; 
                }
                
                ::-webkit-scrollbar-thumb:hover {
                    background: #237bfffb; 
                }

                
                div::-webkit-scrollbar-track {
                    background: none; 
                }
                
                div::-webkit-scrollbar-thumb {
                    background: none; 
                }
                
                div::-webkit-scrollbar-thumb:hover {
                    background: none; 
                }
                table,th,td{
                    border : 5px solid red;
                }
                
                
            </style>
            <body>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>USERNSME</th>
                        <th>EMAIL</th>
                        <th>ENROLLMENT TIME</th>
                    </tr>"""
    data_2=""
    for x in mytb.find({},{}):
        data_2=data_2+"""<tr>
                    <td>"""+str(x['_id'])+"""</td>
                    <td>"""+str(x['username'])+"""</td>
                    <td>"""+str(x['email'])+"""</td>
                    <td>"""+str(x['Enrollment_time'])+"""</td>
                </tr>
       """
    data = data+data_2
    data = data + """</table>
        </body>
        </html>"""
    return HttpResponse(data)



def all_completed_users(request):
    
    course = request.POST.get('completed_users')
    con = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = con["courses"]
    mytb=mydb[course+"_course_completed"]
    data="""<html lang="en">
            <head>
                <title>All data</title>
            </head>
            <style>
                table,tr,td,th {
                    border: 2px solid black;
                    border-collapse: collapse;
                    padding: 5px;
                    color : white;
                }   
                body{
                    height: auto !important;
                    overflow-y:scroll ; 
                    overflow-x: hidden;
                    color: white !important;
                    background-color: #000213;
                    font-family: 'Times New Roman', Times, serif;
                }
                
                ::-webkit-scrollbar {
                    width: 10px;
                }
                
                ::-webkit-scrollbar-track {
                    background: none; 
                }
                
                ::-webkit-scrollbar-thumb {
                    background: #0046af; 
                }
                
                ::-webkit-scrollbar-thumb:hover {
                    background: #237bfffb; 
                }

                
                div::-webkit-scrollbar-track {
                    background: none; 
                }
                
                div::-webkit-scrollbar-thumb {
                    background: none; 
                }
                
                div::-webkit-scrollbar-thumb:hover {
                    background: none; 
                }
                table,th,td{
                    border : 5px solid red;
                }
                
                
            </style>
            <body>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>USERNAME</th>
                        <th>EMAIL</th>
                        <th>COMPLETION TIME</th>
                    </tr>"""
    data_2=""
    for x in mytb.find({},{}):
        data_2=data_2+"""<tr>
                    <td>"""+str(x['_id'])+"""</td>
                    <td>"""+str(x['username'])+"""</td>
                    <td>"""+str(x['email'])+"""</td>
                    <td>"""+str(x['Completion_time'])+"""</td>
                </tr>
       """
    data = data+data_2
    data = data + """</table>
        </body>
        </html>"""
    return HttpResponse(data)


def add_new_course(request):
    cname = request.POST['cname']
    ctopics = request.POST['ctopics']
    ccode = request.POST['ccode']
    
    con = pymongo.MongoClient('mongodb://localhost:27017')
    mydb = con['courses']
    mytb = mydb['all_courses']
    mytb.insert_one({'_id':int(ccode),'course_name': cname,'Total_topics': int(ctopics),'total_users_enrolled':0,'total_users_completed':"0",'courses_launch_date':datetime.now().isoformat()})
    
    return render(request, 'Home_page.html',{'username':'admin'})
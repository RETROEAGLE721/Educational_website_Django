from django.shortcuts import render
from bson import ObjectId
import datetime
import hashlib
import pymongo

def create_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = hashlib.sha256(str(request.POST['pwd']).encode()).hexdigest()
    
    con = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = con['total_users_of_website']
    mytb = mydb['user_details_of_website']
    
    x = mytb.find_one({"email":email},{})
    if x == None: 
        mytb.insert_one({'username':username,'email':email,'password':password,'total_courses_enrolled':0,'total_courses_completed':0,'Registration_time':datetime.datetime.now()})
        return render(request,"login_page.html")
    else:
        return render(request,'new_user.html',{'data':"Account on this email already exists"})



def login_user(request):
    email = request.POST['username']
    pwd = request.POST['pwd']
    if email == "admin" and pwd == "123":
        request.session['_0id']="999"
        request.session['username']='admin'
        return render(request,'Home_page.html',{"username":request.session['username']})
    else:
        pwd = hashlib.sha256(str(pwd).encode()).hexdigest()
        con = pymongo.MongoClient("mongodb://localhost:27017")
        mydb = con['total_users_of_website']
        mytb = mydb['user_details_of_website']
        x =mytb.find_one({'email':email,'password':pwd},{})
        if x:
            _id = str(x['_id'])
            email = x['email']
            username = x['username']
            password = x['password']
        
            if email==email and pwd == password:
                request.session['_0id']=_id
                request.session['username']=username
                request.session['email']=email
                return render(request,'Home_page.html',{"username":username})

    return render(request,'login_page.html',{'data':'Invalid Email or Password'})
        
        
        
def logout_page(request):
    for key in list(request.session.keys()):
        del request.session[key]
    
    return render(request,'Home_page.html',{'username':""})



def java_info_page(request):
    request.session['course_id'] = request.POST.get("java_submit")
    if 'username' not in request.session:
        return render(request,'java_info_page.html',{'username':""})
    else:
        x = check_enrollment(request,int(request.POST.get("java_submit")),request.session['username'])
        if x == None:
            return render(request,'java_info_page.html',{'username':request.session['username']})
        return render(request,'java_info_page.html',{'username':request.session['username'],'course':"101"})



def enroll_in_course(request):
    if 'username' not in request.session:
        return render(request,'login_page.html')
    else:
        course_details = request.POST.get('sub')
        course_details = course_details.split(",")
        request.session['course_id'] = course_details[0]
        request.session['course_name'] = course_details[1]
        enroll_process(request,request.session['_0id'],course_details[1],int(course_details[0]),request.session['username'],request.session['email'])
        return render(request,'Introduction_of_java.html')



def check_value(request):
    a = request.POST.get('sub')
    a = a.split(",")
    ans = request.POST.get('ans')
    if ans == None:
        return render(request,a[1]+'.html',{'ans':"2"})
    else:
        if a[1].isdigit():
            fmcq_progress_report(request,request.session['_0id'],"java","-"+a[1]+"-")
        else:
            progress_report(request,request.session['_0id'],a[1])
        if ans == a[0]:
            return render(request,a[1]+'.html',{'ans':"1"})
    return render(request,a[1]+'.html',{'ans':"0"})
        
        
        
def check_enrollment(reqeust,course_id,username):
    con = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = con['all_users_table']
    mytb= mydb[username]
    x = mytb.find_one({'_id':course_id},{})
    if x == None:
        return None
    else:
        return "helllo"
    
    
    
def course_completion_insert_details(request,_id,course_name,course_id,username,email):
    con = pymongo.MongoClient("mongodb://127.0.0.1:27017")

    mydb = con['courses']
    mytb = mydb[course_name+'_course_completed']
    mytb.insert_one({'_id':_id,'username':username,'email':email,'course_code':course_id ,'course_name':course_name,'Completion_time':datetime.datetime.now().isoformat()})


    mydb = con['all_users_table']
    mytb = mydb[username]
    mytb.update_one({'_id':int(course_id)},{'$set':{'completed':'1','completion_time':datetime.datetime.now().isoformat()}})


    mydb = con['courses']
    mytb = mydb['all_courses']
    x = mytb.find_one({'course_name':course_name},{})
    a = 1 + int(x['total_users_completed'])
    mytb.update_one({'course_name':course_name},{'$set':{'total_users_completed':str(a)}})


    mydb = con['total_users_of_website']
    mytb= mydb['user_details_of_website']
    x = mytb.find_one({'_id':ObjectId(_id)},{})
    a = 1 + int(x['total_courses_completed'])
    mytb.update_one({'_id':ObjectId(_id)},{'$set':{'total_courses_completed':a}})
    
    
    mydb = con['Final_mcq_progress']
    mytb = mydb[course_name]
    mytb.delete_one({'_id':_id})
    
    
    
def enroll_process(reqeust,_id,course_name,course_id,username,email):
    
    
    con = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = con['courses']
    mytb = mydb[course_name]
    mytb.insert_one({'_id': _id,'username': username,'email': email,'Enrollment_time': datetime.datetime.now().isoformat()})


    mydb = con['courses_progress']
    mytb = mydb[course_name]
    data = {'_id':_id,'username':username,'email':email,'intro_of_java':0,'operator2':0,'scanner2':0,'type_casting':0,'if_else':0,'for_loop':0,'switch_':0,'constructor':0,'this':0,'Object_':0,'anonymous_object_':0,'method_':0,'access_modifier':0,'final_class':0,'final_variable_':0,'final_method_':0,'method_overriding_':0,'inheritance_':0,'Single_Inheritance_':0,'muiltilevel_inheritance_':0,'hybrid_inheritance':0,'hierarchical_inheritance_':0,'super':0,'Abstraction':0,'Interface_':0,'exception':0,'try_catch':0,'finally':0}
    mytb.insert_one(data)


    mydb = con['courses']
    mytb= mydb['all_courses']
    x = mytb.find_one({'_id':int(course_id)},{})
    a = 1 + int(x['total_users_enrolled'])
    mytb.update_one({'_id':course_id},{'$set':{'total_users_enrolled':a}})
    
    
    mydb = con['total_users_of_website']
    mytb= mydb['user_details_of_website']
    x = mytb.find_one({'_id':ObjectId(_id)},{})
    a = 1 + int(x['total_courses_enrolled'])
    mytb.update_one({'_id':ObjectId(_id)},{'$set':{'total_courses_enrolled':a}})


    mydb = con['all_users_table']
    mytb = mydb[username]
    mytb.insert_one({'_id':course_id,'course_name':course_name,'completed':0,'Enrollment_time':datetime.datetime.now().isoformat(),'completion_time':"0"})


def final_mcq_insert_new_user(reqeust,_id,course_name,username,email):
    
    con = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = con['Final_mcq_progress']
    mytb= mydb[course_name]
    mytb.insert_one({'_id':_id,'username':username,'email':email,'-1-':0,'-2-':0,'-3-':0,'-4-':0,'-5-':0,'-6-':0,'-7-':0,'-8-':0,'-9-':0,'-10-':0,'-11-':0,'-12-':0,'-13-':0,'-14-':0,'-15-':0,'-16-':0,'-17-':0,'-18-':0,'-19-':0,'-20-':0,'-21-':0,'-21-':0,'-22-':0,'-23-':0,'-22-':0,'-23-':0,'-24-':0,'-25-':0,'-26-':0,'-27-':0,'-28-':0,'-29-':0,'-30-':0})


    mydb = con['courses_progress']
    mytb = mydb[course_name]
    mytb.delete_one({'_id':_id})



def fmcq_progress_report(reqeust,_id,course_name,col_name):

    con = pymongo.MongoClient('mongodb://localhost:27017')
    mydb = con['Final_mcq_progress']
    mytb= mydb[course_name]
    mytb.update_one({'_id':_id},{'$set':{col_name:1}})



def progress_report_check(request):
    a = 0
    course = request.POST.get('sub2')
    con = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = con['Final_mcq_progress']
    mytb = mydb['java']
    _id = request.session['_0id']
    x = mytb.find_one({'_id':_id},{})
    for v in range(1,31):
        a = a + x["-"+str(v)+"-"]
    if a == 30:
        course_completion_insert_details(request,request.session['_0id'],course,request.session['course_id'],request.session['username'],request.session['email'])
        return render(request,"course_completion.html")
    return render(request,"complete_all_MCQs.html")
    
    
    
    
def progress_report(reqeust,_id,col_name):

    con = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = con['courses_progress']
    mytb = mydb['java']
    mytb.update_one({'_id':_id},{'$set':{col_name:1}})
    
    

def check_progress(reqeust):
    a = 0
    con = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = con['courses_progress']
    mytb = mydb['java']
    x = mytb.find_one({'_id':reqeust.session['_0id']},{})
    g = list(x)
    g.pop(0)
    g.pop(0)
    g.pop(0)
    for c in g:
        a = a + int(x[c])
    if a == 28:
        final_mcq_insert_new_user(reqeust,reqeust.session['_0id'],"java",reqeust.session['username'],reqeust.session['email'])
        return render(reqeust,'1.html')
    return render(reqeust,'fmcq_info.html',{'complete':'Please complete all MCQs befor stating test'})
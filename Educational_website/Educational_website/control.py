from django.shortcuts import render
from . import model

def Home_page(request):
    if 'username' not in  request.session:
        return render(request,'Home_page.html',{'username':""})
    else:
        return render(request,'Home_page.html',{'username':request.session['username']})

def login_page(request):
    return render(request,'login_page.html')

def new_user(request):
    return render(request,'new_user.html')

def list_of_courses(request):
    if 'username' not in request.session:
        return render(request,'list_of_courses.html',{'username':""})
    else:
        return render(request,'list_of_courses.html',{'username':request.session['username']})

def other_program(request):
    return render(request,'other_program.html')

def check_value(request):
    return render(request,'other_program.html')

def PT(request):
    File_name = request.POST.get('sub1')
    return render(request,File_name+'.html')

def First_PT(request):
    return render(request,'Introduction_of_java.html')

def F1(request):
    a = str(request.POST.get('sub2'))
    return render(request,a+'.html')

def F2(request):
    return render(request,'1.html')

def Introduction_of_java(request):
    return render(request,'Introduction_of_java.html')

def Operator(request):
    return render(request,'Operator.html')

def Scanner(request):
    return render(request,'Scanner.html')

def Typecasting(request):
    return render(request,'Typecasting.html')

def Ifelse(request):
    return render(request,'Ifelse.html')

def loop(request):
    return render(request,'loop.html')

def Switch(request):
    return render(request,'Switch.html')

def Class_Constructor(request):
    return render(request,'Class_Constructor.html')

def This_Keyword(request):
    return render(request,'This_Keyword.html')

def Object(request):
    return render(request,'Object.html')

def Anonymous_object(request):
    return render(request,'Anonymous_object.html')

def Method(request):
    return render(request,'Method.html')

def Access_Modifiers(request):
    return render(request,'Access_Modifiers.html')

def FinalClass1(request):
    return render(request,'FinalClass1.html')

def Final_Variable(request):
    return render(request,'Final_Variable.html')

def Final_method(request):
    return render(request,'Final_method.html')

def Method_overriding(request):
    return render(request,'Method_overriding.html')

def Inheritance(request):
    return render(request,'Inheritance.html')

def Single_Inheritance(request):
    return render(request,'Single_Inheritance.html')

def Muiltilevel_Inheritance(request):
    return render(request,'Muiltilevel_Inheritance.html')

def Muiltiple_hybrid_Inheritance(request):
    return render(request,'Muiltiple_hybrid_Inheritance.html')

def Hierarchical_inheritance(request):
    return render(request,'Hierarchical_inheritance.html')

def SuperKeyword(request):
    return render(request,'SuperKeyword.html')

def Abstract_class_and_method(request):
    return render(request,'Abstract_class_and_method.html')

def interface(request):
    return render(request,'interface.html')

def exception_handling(request):
    return render(request,'exception_handling.html')

def try_catch_block(request):
    return render(request,'try_catch_block.html')

def finally_block(request):
    return render(request,'finally_block.html')

def FM1(request):
    return render(request,'1.html')

def FM2(request):
    return render(request,'2.html')

def FM3(request):
    return render(request,'3.html')

def FM4(request):
    return render(request,'4.html')

def FM5(request):
    return render(request,'5.html')

def FM6(request):
    return render(request,'6.html')

def FM7(request):
    return render(request,'7.html')

def FM8(request):
    return render(request,'8.html')

def FM9(request):
    return render(request,'9.html')

def FM10(request):
    return render(request,'10.html')

def FM10(request):
    return render(request,'10.html')

def FM11(request):
    return render(request,'11.html')

def FM12(request):
    return render(request,'12.html')

def FM13(request):
    return render(request,'13.html')

def FM14(request):
    return render(request,'14.html')

def FM15(request):
    return render(request,'15.html')

def FM16(request):
    return render(request,'16.html')

def FM17(request):
    return render(request,'17.html')

def FM18(request):
    return render(request,'18.html')

def FM19(request):
    return render(request,'19.html')

def FM20(request):
    return render(request,'20.html')

def FM21(request):
    return render(request,'21.html')

def FM22(request):
    return render(request,'22.html')

def FM23(request):
    return render(request,'23.html')

def FM24(request):
    return render(request,'24.html')

def FM25(request):
    return render(request,'25.html')

def FM26(request):
    return render(request,'26.html')

def FM27(request):
    return render(request,'27.html')

def FM28(request):
    return render(request,'28.html')

def FM29(request):
    return render(request,'29.html')

def FM30(request):
    return render(request,'30.html')

def fmcq_info(request):
    return render(request,'fmcq_info.html')

def course_completion(request):
    return render(request,'course_completion.html')

def new_course(request):
    return render(request, 'new_course.html')
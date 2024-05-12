"""Miniproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import control
from . import model
from . import admin_model

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', control.Home_page,name="Home_page"),
    path('Home_page', control.Home_page,name="Home_page"),
    path('login_page', control.login_page,name="login_page"),
    path('login_user', model.login_user,name="login_user"),
    path('enroll_process', model.enroll_process,name="enroll_process"),
    path('logout_page', model.logout_page,name="logout_page"),
    path('new_user', control.new_user,name="new_user"),
    path('course_completion', control.course_completion,name="course_completion"),
    path('create_user', model.create_user,name="create_user"),
    path('check_value', model.check_value,name="create_usercheck_value"),
    path('enroll_in_course', model.enroll_in_course,name="enroll_in_course"),
    path('list_of_courses', control.list_of_courses,name="list_of_courses"),
    path('other_program', control.other_program,name="other_program"),
    path('java_info_page', model.java_info_page,name="java_info_page"),
    path('F1',control.F1,name='F1'),
    path('F2',control.F2,name='F2'),
    path('PT',control.PT,name='PT'),
    path('First_PT',control.First_PT,name='First_PT'),
    path('Typecasting',control.Typecasting,name='Typecasting'),
    path('Scanner',control.Scanner,name='Scanner'),
    path('Operator',control.Operator,name='Operator'),
    path('Introduction_of_java',control.Introduction_of_java,name='Introduction_of_java'),
    path('Ifelse',control.Ifelse,name='Ifelse'),
    path('loop',control.loop,name='loop'),
    path('Switch',control.Switch,name='Switch'),
    path('Class_Constructor',control.Class_Constructor,name='Class_Constructor'),
    path('This_Keyword',control.This_Keyword,name='This_Keyword'),
    path('Object',control.Object,name='Object'),
    path('Anonymous_object',control.Anonymous_object,name='Anonymous_object'),
    path('Method',control.Method,name='Method'),
    path('Access_Modifiers',control.Access_Modifiers,name='Access_Modifiers'),
    path('FinalClass1',control.FinalClass1,name='FinalClass1'),
    path('Final_Variable',control.Final_Variable,name='Final_Variable'),
    path('Final_method',control.Final_method,name='Final_method'),
    path('Method_overriding',control.Method_overriding,name='Method_overriding'),
    path('Inheritance',control.Inheritance,name='Inheritance'),
    path('Single_Inheritance',control.Single_Inheritance,name='Single_Inheritance'),
    path('Muiltilevel_Inheritance',control.Muiltilevel_Inheritance,name='Muiltilevel_Inheritance'),
    path('Muiltiple_hybrid_Inheritance',control.Muiltiple_hybrid_Inheritance,name='Muiltiple_hybrid_Inheritance'),
    path('Hierarchical_inheritance',control.Hierarchical_inheritance,name='Hierarchical_inheritance'),
    path('SuperKeyword',control.SuperKeyword,name='SuperKeyword'),
    path('Abstract_class_and_method',control.Abstract_class_and_method,name='Abstract_class_and_method'),
    path('interface',control.interface,name='interface'),
    path('exception_handling',control.exception_handling,name='exception_handling'),
    path('try_catch_block',control.try_catch_block,name='try_catch_block'),
    path('finally_block',control.finally_block,name='finally_block'),
    path('FM1',control.FM1,name='FM1'),
    path('FM2',control.FM2,name='FM2'),
    path('FM3',control.FM3,name='FM3'),
    path('FM4',control.FM4,name='FM4'),
    path('FM5',control.FM5,name='FM5'),
    path('FM6',control.FM6,name='FM6'),
    path('FM7',control.FM7,name='FM7'),
    path('FM8',control.FM8,name='FM8'),
    path('FM9',control.FM9,name='FM9'),
    path('FM10',control.FM10,name='FM10'),
    path('FM11',control.FM11,name='FM11'),
    path('FM12',control.FM12,name='FM12'),
    path('FM13',control.FM13,name='FM13'),
    path('FM14',control.FM14,name='FM14'),
    path('FM15',control.FM15,name='FM15'),
    path('FM16',control.FM16,name='FM16'),
    path('FM17',control.FM17,name='FM17'),
    path('FM18',control.FM18,name='FM18'),
    path('FM19',control.FM19,name='FM19'),
    path('FM20',control.FM20,name='FM20'),
    path('FM21',control.FM21,name='FM21'),
    path('FM22',control.FM22,name='FM22'),
    path('FM23',control.FM23,name='FM23'),
    path('FM24',control.FM24,name='FM24'),
    path('FM25',control.FM25,name='FM25'),
    path('FM26',control.FM26,name='FM26'),
    path('FM27',control.FM27,name='FM27'),
    path('FM28',control.FM28,name='FM28'),
    path('FM29',control.FM29,name='FM29'),
    path('FM30',control.FM30,name='FM30'),
    path('fmcq_info',control.fmcq_info,name='fmcq_info'),
    path('check_progress',model.check_progress,name='check_progress'),
    path('progress_report_check',model.progress_report_check,name='progress_report_check'),
    path('view_website_all_users',admin_model.view_website_all_users,name='view_website_all_users'),
    path('new_course',control.new_course,name='new_course'),
    path('add_new_course',admin_model.add_new_course,name='add_new_course'),
    path('all_enrolled_users',admin_model.all_enrolled_users,name='all_enrolled_users'),
    path('all_completed_users',admin_model.all_completed_users,name='all_completed_users'),
    
]

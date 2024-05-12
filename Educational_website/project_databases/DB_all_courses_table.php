<?php

$course = "JAVA";
// $course = $_POST['course'];
 $con=new mysqli("localhost","root","");
 $con->query("CREATE DATABASE Courses");
 $con->close();


 $con=mysqli_connect("localhost","root","","Courses");

 $q1="CREATE TABLE $course(
     id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
     Username varchar(20) not null,
     Email varchar(20) not null,
     Completed varchar(20) not null,
     Reg_time timestamp

 )";
 mysqli_query($con,$q1);
 mysqli_close($con);


 $con=mysqli_connect("localhost","root","","Courses");

 $q1="CREATE TABLE all_courses(
    course_code INT(10) not null PRIMARY KEY,
     Name_of_courses varchar(20) not null,
     total_topics varchar(20) not null,
     total_enrolled_users varchar(20) not null,
     total_users_completed varchar(20) not null,
     Reg_time timestamp

 )";
 mysqli_query($con,$q1);
 mysqli_close($con);
header('Location:http://localhost/php/project_login/login_page.php');
?>
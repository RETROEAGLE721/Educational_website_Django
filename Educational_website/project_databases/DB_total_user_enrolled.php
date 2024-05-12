<?php

$con=mysqli_connect("localhost","root","","all_courses_details");

$q1="CREATE TABLE all_users_enrolled_courses(
    Number_of_users INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    Username varchar(20) not null,
    Email varchar(50) not null,
    course_code INT(10) not null,
    course_name varchar(20) not null,
    Course_Completed varchar(20) not null,
    Reg_time timestamp

)";
mysqli_query($con,$q1);
mysqli_close($con);
header('Location:http://localhost/php/project_login/login_page.php');
?>
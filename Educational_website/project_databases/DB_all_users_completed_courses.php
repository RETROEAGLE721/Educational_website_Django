<?php
 $con=new mysqli("localhost","root","");
 $con->query("CREATE DATABASE all_courses_details");
 $con->close();

$con=mysqli_connect("localhost","root","","all_courses_details");

$q1="CREATE TABLE all_users_completed_courses(
    id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    Username varchar(20) not null,
    Email varchar(20) not null,
    course_code INT(10) not null,
    Course_name varchar(20) not null,
    Reg_time timestamp

)";
mysqli_query($con,$q1);
mysqli_close($con);
header('Location:http://localhost/php/project_login/login_page.php');

?>
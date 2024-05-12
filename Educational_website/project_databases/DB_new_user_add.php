<?php

if (true) {
 $con=new mysqli("localhost","root","");
 $con->query("CREATE DATABASE total_users_of_website");
 $con->close();

 $con=mysqli_connect("localhost","root","","total_users_of_website");

 $q1="CREATE TABLE user_details_of_website(
     id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
     username varchar(20) not null,
     email varchar(50) not null,
     paassword varchar(20) not null,
     total_courses_enrolled INT(20) not null,
     total_courses_completed INT(20) not null,
     Reg_time timestamp

 )";

 mysqli_query($con,$q1);
 mysqli_close($con);

 $con = new mysqli("localhost","root","");
 $con->query("CREATE DATABASE all_users_table");
 $con->close();

$username=$_POST['username'];
$email=$_POST['email'];
$pwd=$_POST['pwd'];

$con=mysqli_connect("localhost","root","","total_users");

mysqli_query($$con,"INSERT INTO user_details(username,email,paassward,total_courses_enrolled,total_courses_completed)VALUES('$username','$email','$pwd','0','0')");
mysqli_close($con);
header("location:http://localhost/php/project_login/login_page.php");
 } 
?>
<?php

$username = "Dhairya";
// $username = $_POST['username'];

 $con=mysqli_connect("localhost","root","","all_users_table");

 $q1="CREATE TABLE $username(
     id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
     course_code INT(10) not null,
     Name_of_courses varchar(20) not null,
     Completed varchar(20) not null,
     Reg_time timestamp

 )";

 mysqli_query($con,$q1);
 mysqli_close($con);
 header('Location:http://localhost/php/project_login/login_page.php');
?>
<?php
 $con = new mysqli("localhost","root","");
 $con->query("CREATE DATABASE courses_progress");
 $con->close();

$con=mysqli_connect("localhost","root","","courses_progress");

$q1="CREATE TABLE java(
    Number_of_users INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    Username varchar(20) not null,
    Email varchar(50) not null,
    Course_Completed varchar(20) not null,
    Introducation_Of_Java int(1) DEFAULT '0' not null, 
    Operators int(1) DEFAULT '0' not null, 
    Scanner int(1) DEFAULT '0' not null, 
    Type_Casting int(1) DEFAULT '0' not null, 
    if_else int(1) DEFAULT '0' not null, 
    Loops int(1) DEFAULT '0' not null, 
    Switch int(1) DEFAULT '0' not null, 
    Class_and_Constructor int(1) DEFAULT '0' not null, 
    This_Keyword int(1) DEFAULT '0' not null, 
    Object_ int(1) DEFAULT '0' not null, 
    Anonymous_Object int(1) DEFAULT '0' not null, 
    Method int(1) DEFAULT '0' not null, 
    Access_Modifiers int(1) DEFAULT '0' not null, 
    FinalClass int(1) DEFAULT '0' not null, 
    Final_Variable int(1) DEFAULT '0' not null, 
    Final_Method int(1) DEFAULT '0' not null, 
    Method_Overriding int(1) DEFAULT '0' not null, 
    Inheritance int(1) DEFAULT '0' not null, 
    Single_Inheritance int(1) DEFAULT '0' not null, 
    Muiltilevel_Inheritance int(1) DEFAULT '0' not null, 
    Muiltiple_hybrid_Inheritance int(1) DEFAULT '0' not null, 
    Hierarchical_Inheritance int(1) DEFAULT '0' not null, 
    Super_Keyword int(1) DEFAULT '0' not null, 
    Abstract_Class_And_Method int(1) DEFAULT '0' not null, 
    Interface int(1) DEFAULT '0' not null, 
    Exception_handling int(1) DEFAULT '0' not null, 
    try_catch int(1) DEFAULT '0' not null, 
    finally_Block int(1) DEFAULT '0' not null

)";
mysqli_query($con,$q1);
mysqli_close($con);
// header('Location:http://localhost/php/project_login/login_page.php');
?>
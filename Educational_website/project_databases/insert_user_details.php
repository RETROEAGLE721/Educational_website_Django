<?php
ob_start();
session_start();

$id=$_SESSION['id7'];
$ccode = $_SESSION['ccode']; 
$cname = $_SESSION['cname']; 
$username=$_SESSION['username'];
$email=$_SESSION['email'];

$con=mysqli_connect("localhost","root","","all_courses_details");
$q1 = "INSERT INTO all_users_enrolled_courses(Username,Email,course_code,course_name,Course_Completed) VALUES ('$username','$email','$ccode','$cname','0')";
mysqli_query($con,$q1);
mysqli_close($con);

$con = mysqli_connect("localhost","root","","all_users_table");
$q2 = "INSERT INTO $username(course_code,Name_of_courses,Completed) VALUES ('$ccode','$cname','0')";
mysqli_query($con,$q2);
mysqli_close($con);


$con = mysqli_connect("localhost","root","","courses");
$q3 = "INSERT INTO $cname(Username,Email,Completed) VALUES ('$username','$email','0')";
mysqli_query($con,$q3);
mysqli_close($con);


  $con=mysqli_connect("localhost","root","","courses");
  $q4 = "SELECT total_enrolled_users from all_courses where course_code ='$ccode'";
  $re=mysqli_query($con,$q4);
  while($row=mysqli_fetch_array($re)){

    $a = $row['total_enrolled_users'];

  }

    $b = $a + 1 ;
    $q5="UPDATE all_courses SET total_enrolled_users='$b' WHERE course_code = '$ccode'";
    mysqli_query($con,$q5);
    mysqli_close($con);



  $con=mysqli_connect("localhost","root","","total_users_of_website");
  $q6 = "SELECT total_courses_enrolled from user_details_of_website where id ='$id'";
  $re=mysqli_query($con,$q6);
  while($row=mysqli_fetch_array($re)){

  $a = $row['total_courses_enrolled'];

    }
    $b = $a + 1 ;

    $q7="UPDATE user_details_of_website SET total_courses_enrolled='$b' WHERE id = '$id'";
    mysqli_query($con,$q7);
    mysqli_close($con);

    $path = $_SESSION['cpath'];
    header("Location:$path");
?>
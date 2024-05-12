<?php
ob_start();
session_start();


    $id=$_SESSION['id7'];
    $ccode = $_SESSION['ccode']; 
    $cname = $_SESSION['cname']; 
    $username=$_SESSION['username'];
    $email=$_SESSION['email'];


    $con=mysqli_connect("localhost","root","","all_courses_details");
    $q1 = "INSERT INTO all_users_completed_courses(Username,Email,course_code,course_name) VALUES ('$username','$email','$ccode','$cname')";
    mysqli_query($con,$q1);
    mysqli_close($con);


    $con=mysqli_connect("localhost","root","","all_courses_details");
    $q2 = "UPDATE all_users_enrolled_courses SET Course_Completed='1' WHERE Email='$email'";
    mysqli_query($con,$q2);
    mysqli_close($con);


    $con=mysqli_connect("localhost","root","","all_users_table");
    $q3 = "UPDATE $username SET Completed='1' WHERE course_code ='$ccode'";
    mysqli_query($con,$q3);
    mysqli_close($con);


    $con=mysqli_connect("localhost","root","","courses");
    $q4 = "SELECT total_users_completed from all_courses where course_code ='$ccode'";
    $re=mysqli_query($con,$q4);
    while($row=mysqli_fetch_array($re)){

    $a = $row['total_users_completed'];

    }
    $b = $a + 1 ;

    $q5="UPDATE all_courses SET total_users_completed='$b' WHERE course_code = '$ccode'";
    mysqli_query($con,$q5);
    mysqli_close($con);



    $con=mysqli_connect("localhost","root","","courses");
    $q6 = "INSERT INTO $cname(Username,Email,Completed) VALUES ('$username','$email','1')";
    mysqli_query($con,$q6);
    mysqli_close($con);



    $con=mysqli_connect("localhost","root","","total_users_of_website");
    $q7 = "SELECT total_courses_completed from user_details_of_website where id ='$id'";
    $re=mysqli_query($con,$q7);
    while($row=mysqli_fetch_array($re)){

    $a = $row['total_courses_completed'];

    }
    $b = $a + 1 ;

    $q8="UPDATE user_details_of_website SET total_courses_completed='$b' WHERE id = '$id'";
    mysqli_query($con,$q8);
    mysqli_close($con);


    $path = $_SESSION['cpath'];
    header("Location:$path");


?>

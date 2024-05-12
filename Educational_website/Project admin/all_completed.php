<?php
session_start();
?>
<html>
<body>

     <table border ="3" align="center">
        <tr>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;id &nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;Username&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;Email&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;course code&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;course name&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;Reg time&nbsp;&nbsp;&nbsp;&nbsp;</th>
        </tr>

<?php
              $con = mysqli_connect("localhost","root","","all_courses_details");

              $rs=mysqli_query($con,"SELECT * FROM all_users_completed_courses"); 
              
              while($row=mysqli_fetch_array($rs))

{

?>

  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row['id']; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row["Username"]; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row["Email"]; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row["course_code"]; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row['Course_name']; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row['Reg_time']; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>

  </tr>

<?php                             

}

?>
</table>

</body>

</html>
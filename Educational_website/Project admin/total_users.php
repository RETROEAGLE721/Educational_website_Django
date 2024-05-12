<?php
session_start();
?>
<html>
<body>

     <table border ="3" align="center">
        <tr>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;id &nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;username&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;email&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;total_courses_enrolled&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;total_courses_completed&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;Reg_time&nbsp;&nbsp;&nbsp;&nbsp;</th>
        </tr>

<?php
              $con = mysqli_connect("localhost","root","","total_users_of_website");

              $rs=mysqli_query($con,"SELECT * FROM user_details_of_website"); 
              
              while($row=mysqli_fetch_array($rs))

{

?>

  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row['id']; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row["username"]; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row["email"]; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row["total_courses_enrolled"]; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row['total_courses_completed']; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row['Reg_time']; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>

  </tr>

<?php                             

}

?>
</table>

</body>

</html>
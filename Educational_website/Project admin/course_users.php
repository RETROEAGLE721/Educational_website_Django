<?php
session_start();
?>
<html>
<body>

     <table border ="3" align="center">
        <tr>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;course_code &nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;Name_of_courses	&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;total_topics&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;total_enrolled_users&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;total_users_completed&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;Reg_time&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;Delete&nbsp;&nbsp;&nbsp;&nbsp;</th>
        </tr>

<?php
              $con = mysqli_connect("localhost","root","","courses");

              $rs=mysqli_query($con,"SELECT * FROM all_courses"); 
              
              while($row=mysqli_fetch_array($rs))

{

?>

  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row['course_code']; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row["Name_of_courses"]; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row["total_topics"]; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row["total_enrolled_users"]; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row["total_users_completed"]; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row['Reg_time']; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <form method="post">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<button name="delete" value="<?php echo $row["course_code"]; ?>">Delete</button>&nbsp;&nbsp;&nbsp;&nbsp;</td>
    </form>
  </tr>

<?php                             

}

?>
</table>

</body>

</html>
<?php
if (isset($_POST['delete'])) {
    $ccode=$_POST['delete'];
    $conn=mysqli_connect("localhost","root","","courses");
    mysqli_query($conn,"DELETE FROM all_courses WHERE course_code='$ccode'");
}
?>
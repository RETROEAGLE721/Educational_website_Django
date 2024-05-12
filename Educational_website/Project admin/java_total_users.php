<?php
session_start();
?>
<html>
<body>

     <table border ="3" align="center">
        <tr>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;Number_of_users &nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;Username&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;Email&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;Completed&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>&nbsp;&nbsp;&nbsp;&nbsp;Reg_time&nbsp;&nbsp;&nbsp;&nbsp;</th>
        </tr>

<?php
              $con = mysqli_connect("localhost","root","","courses");

              $rs=mysqli_query($con,"SELECT * FROM java"); 
              
              while($row=mysqli_fetch_array($rs))

{

?>

  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row['Number_of_users']; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row["Username"]; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row["Email"]; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row["Completed"]; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<?php echo $row['Reg_time']; ?> &nbsp;&nbsp;&nbsp;&nbsp;</td>
    <form method="post">
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<button name="delete" value="<?php echo $row["Email"]; ?>">Delete</button>&nbsp;&nbsp;&nbsp;&nbsp;</td>
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
    $email=$_POST['delete'];
    $conn=mysqli_connect("localhost","root","","courses");
    mysqli_query($conn,"DELETE FROM java WHERE Email='$email'");
}
?>
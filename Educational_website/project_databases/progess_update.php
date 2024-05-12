<?php
session_start();

$path = $_SESSION['cpath'];
header('Location:'.$path);


?>
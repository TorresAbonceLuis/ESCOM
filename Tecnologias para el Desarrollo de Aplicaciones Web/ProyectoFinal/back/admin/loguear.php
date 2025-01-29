<?php
    require("../BD/conexionBD.php");
    session_start();
    $usuario = $_POST['usuario'];
    $contraseña = $_POST['contraseña'];

    $q = "select count(*) as contar from admin where usuario = '$usuario' and contraseña = '$contraseña'";
    $sql = mysqli_query($conexion,$q);
    $respSql = mysqli_fetch_array($sql);

    if ($respSql['contar']>0){
        $_SESSION['username'] = $usuario;
        header("location: ../../front/admin.php");//cambiar ruta a admin
    }else{
        header("location: ../../front/login.html");
    }
?>
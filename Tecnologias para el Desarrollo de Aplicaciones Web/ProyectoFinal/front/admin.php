<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <!--Import materialize.css-->
    <link type="text/css" rel="stylesheet" href="css/bootstrap.css" media="screen,projection" />
    <!-- <link type="text/css" rel="stylesheet" href="css/materialize.css" media="screen,projection" /> -->
    <link type="text/css" rel="stylesheet" href="css/cssProyecto.css" media="screen,projection" />
    
    <link type="text/css" rel="stylesheet" href="css/custom.css" />
    <!--Jquery-->
    <script type="text/javascript" src="js/jquery-3.6.0.js"></script>
    <script type="text/javascript" src="js/admin.js"></script>
    <script type="text/javascript" src="js/bootstrap.js"></script>
    <script type="text/javascript" src="js/materialize.js"></script>
    
    <title>.::Admin::.</title>

</head>

<body>
    <header>
        <nav id="navegacion"></nav>
    </header>
    <div class="container">   
        <h1>Administrador</h1>
        <div class="collection" id="alumnos"></div>
    </div>

    <footer id="futer"></footer>
    <p id="hola">Prueba :D</p>
</body>
</html>
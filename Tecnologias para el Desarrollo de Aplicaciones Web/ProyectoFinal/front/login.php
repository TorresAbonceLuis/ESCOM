<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!--Import Google Icon Font-->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <!--Import materialize.css-->
    <link type="text/css" rel="stylesheet" href="css/materialize.css" media="screen,projection" />
    <!--Let browser know website is optimized for mobile-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!--Jquery-->
    <script type="text/javascript" src="js/jquery-3.6.0.js"></script>
    <script type="text/javascript" src="js/materialize.js"></script>
    <title>.::Login::.</title>
    <script>
        $(document).ready(function() {
            $("#navegacion").load("./compartidos/barranav.html");
            $("#futer").load("./compartidos/futer.html");
            $("#btn-reset").click(function() {
                $("#formula").trigger('reset');
            });
        });
    </script>
</head>

<body>
    <header id="navegacion"></header>
    <h1>Bienvenido</h1>
    <form id="formula" action="../back/api.php" method="get">
        <fieldset>
            <legend>ADMIN</legend>
            <div class="row">
                <div class="input-field col s6">
                    <input id="correo" name="correo" type="text">
                    <label for="correo">Correo</label>
                </div>
            </div>
            <div class="row">
                <div class="input-field col s6">
                    <input id="contrasena" name="contrasena" type="text">
                    <label for="contrasena">Contraseña</label>
                </div>
            </div>
        </fieldset>
        <div class="row">
            <a id="btn-reset" class="waves-effect waves-light btn">Limpiar</a>
            <button id="btn-submit" class="btn btn-primary" type="submit" name="action">
                        Enviar
            </button>
        </div>
    </form>

    <footer id="futer"></footer>
</body>

</html>
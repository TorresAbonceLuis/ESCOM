<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!--Import Google Icon Font-->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <!--Import materialize.css-->
    <link type="text/css" rel="stylesheet" href="css/bootstrap.css" media="screen,projection" />
    <link type="text/css" rel="stylesheet" href="css/custom.css" />
    <!--Let browser know website is optimized for mobile-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!--Jquery-->
    <script type="text/javascript" src="js/jquery-3.6.0.js"></script>
    <script type="text/javascript" src="js/materialize.js"></script>
    <title>.::Recuperar PDF::.</title>
    <script>
        $(document).ready(function() {
            $("#navegacion").load("./compartidos/barranav.html");
            $("#futer").load("./compartidos/futer.html");
            var alumno;
            $("#formula").submit(function(event) {
                event.preventDefault();

                var form = $(this);

                var formData = {
                    folio: $("#folio").val(),
                    accion: "recuperar",
                };
                alumno = formData;
                var actionUrl = form.attr('action') + "?folio=" + formData.folio;
                window.open(actionUrl, '_self');
            });
            $("#btn-reset").click(function() {
                $("#formula").trigger('reset');
            });
            $('#recuperar').click(function() {
                let direc = "../back/pdf/generatePDF.php?folio=" + alumno.folio;
                window.open(direc, '_blank');
            });

        });
    </script>
</head>

<body>
    <header id="navegacion"></header>
    <div class="container">
      <div class="mt-5">
        <form id="formula" action="../back/pdf/generatePDF.php" method="get">
            <fieldset class="form-group border p-3">
                <legend class="w-auto">BUSCAR COMPROBANTE DE CITA</legend>
                <div class="mb-3">
                    <input id="folio" name="folio" type="text" data-length="10" placeholder="Folio (Boleta)" class="form-control username">
                </div>
                <button id="recuperar" class="btn btn-primary" type="submit" name="action"> Recuperar
                </button>
        </form>
        </fieldset>
        </div>
    </div>
</body>
<footer id="futer"></footer>

</html>
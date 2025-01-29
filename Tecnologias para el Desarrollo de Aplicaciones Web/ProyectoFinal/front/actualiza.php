<?php
$bole = $_GET['folio'];
$boleto = ""
?>


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
    <title>.::Actualiza::.</title>
    <script>
        $(document).ready(function() {
            $("#navegacion").load("./compartidos/barranavadmin.html");
            $("#futer").load("./compartidos/futer.html");
            $('select').formSelect(); //jala select
            $('input#input_text, textarea#textarea2').characterCounter(); // jala counter

            $('.datepicker').datepicker({
                monthsFull: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
                monthsShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
                weekdaysFull: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
                weekdaysShort: ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'],
                selectMonths: true,
                selectYears: 100, // Puedes cambiarlo para mostrar más o menos años
                today: 'Hoy',
                clear: 'Limpiar',
                close: 'Ok',
                labelMonthNext: 'Siguiente mes',
                labelMonthPrev: 'Mes anterior',
                labelMonthSelect: 'Selecciona un mes',
                labelYearSelect: 'Selecciona un año',
            });


            // Old way
            // $('select').material_select();
        });
    </script>
</head>

<body>
<div class="row blue lighten-4">
    <header id="navegacion"></header> 
    <div class="row"></div>  
    <div class="center-align">
    <h1 id="titulo">Bienvenido a la Actualizacion de Registro</h1>
    </div>
    <form action="../back/hola.php" method="get" id="formulario">
        <div id="tablas">
            <div id="tabla1">
                <div class="card blue lighten-5 z-depth-3z-depth-3">
        <fieldset>
            <legend><h6>DATOS GENERALES</h6></legend>
            <div class="input-field col s12 m6">
                <select class="icons">
                    <option value="" disabled selected>Seleccione su CENDI</option>
                    <option value="1" data-icon="https://picsum.photos/100/100">Amalia Solórzano de Cárdenas
                    </option>
                    <option value="2" disabled data-icon="https://picsum.photos/100/100">cendi 2</option>
                    <option value="3" disabled data-icon="https://picsum.photos/100/100">cendi 3</option>
                </select>
                <label>Cendi</label>
            </div>


            <div class="file-field input-field">
                <div class="btn">
                    <span>Foto</span>
                    <input type="file">
                </div>
                <div class="file-path-wrapper">
                    <input class="file-path validate" type="text">
                </div>
            </div>

            <div class="row">
                <div class="input-field col s6">
                    <input id="folio" name="folio" type="text" data-length="10">
                    <label for="folio">Folio (Boleta)</label>
                </div>
            </div>

            <div class="row">
                <div class="input-field col s6">
                    <input id="grupo" type="text" data-length="5">
                    <label for="grupo">Grupo</label>
                </div>
            </div>
        </fieldset>
    </div>
        </div>
        <div id="tabla2">
            <div class="card blue lighten-5 z-depth-3">
        <fieldset>
            
            <legend><h6>DATOS DEL NIÑO O DE LA NIÑA</h6></legend>
            <div class="row">

                <div class="input-field col s6">
                    <input id="primer_apellido" type="text" class="validate">
                    <label for="primer_apellido">Primer Apellido</label>
                </div>
                <div class="input-field col s6">
                    <input id="segundo_apellido" type="text" class="validate">
                    <label for="segundo_apellido">Segundo Apellido</label>
                </div>
                <div class="input-field col s6">
                    <input id="nombre" type="text" class="validate">
                    <label for="nombre">Nombre(s)</label>
                </div>
                <div class="row">
                    <div class="input-field col s12">
                        <input id="fecha" type="text" class="datepicker">
                        <label for="fecha">Fecha de Nacimiento</label>
                    </div>
                </div>
                <div class="row">
                    <div class="input-field col s12">
                        <input id="email" type="email" class="validate">
                        <label for="email">Email</label>
                        <span class="helper-text" data-error="Invalido" data-success="Valido">Escriba una direccion
                            valida</span>
                    </div>
                </div>
                <div class="input-field col s6">
                    <input id="nombre" type="text" class="validate">
                    <label for="nombre">Edad</label>
                </div>

                <div class="input-field col s6">
                    <input id="curp" type="text" data-length="18">
                    <label for="curp">CURP</label>
                </div>



            </div>
            <div class="row">

        </fieldset>
    </div>
    </div>
    <div id="tabla3">
        <div class="card blue lighten-5 z-depth-3">
        <fieldset>
            <legend><h6>DATOS DEL O LA DERECHOHABIENTE:</h6></legend>
            <div class="row">
                <div class="input-field col s12 s6 m4">
                    <input id="primer_apellido_derecho" type="text" class="validate">
                    <label for="primer_apellido_derecho">Primer Apellido</label>
                </div>
                <div class="input-field col s12 s6 m4">
                    <input id="segundo_apellido_derecho" type="text" class="validate">
                    <label for="segundo_apellido_derecho">Segundo Apellido</label>
                </div>
                <div class="input-field col s12 s6 m4">
                    <input id="nombre_derecho" type="text" class="validate">
                    <label for="nombre_derecho">Nombre(s)</label>
                </div>
                <div class="input-field col s12 m12 l12">
                    <input id="domicilio" type="text" class="validate">
                    <label for="domicilio">Domicilio particular (Calle, no. Ext., no. Int., Colonia, Alcaldía o
                        municipio, Entidad federativa, C.P.</label>
                </div>
                <div class="input-field col s12 s6 m4">
                    <input id="telefono_fijo" type="text" class="validate">
                    <label for="telefono_fijo">Telefono Fijo</label>
                </div>
                <div class="input-field col s12 s6 m4">
                    <input id="telefono_celular" type="text" class="validate">
                    <label for="telefono_celular">Telefono celular</label>
                </div>
                <div class="row">
                    <div class="input-field col s12 s6 m4">
                        <input id="email_derecho" type="email" class="validate">
                        <label for="email_derecho">Email</label>
                        <span class="helper-text" data-error="Invalido" data-success="Valido">Escriba una direccion
                            valida</span>
                    </div>
                </div>
                <div class="input-field col s12 s6">
                    <select>
                        <option value="" disabled selected>Escoja su ocupacion</option>
                        <option value="1">Docente</option>
                        <option value="2">PAAE</option>
                        <option value="3">Funcionario(a)</option>
                    </select>
                    <label>Ocupacion</label>
                </div>

                <div class="input-field col s12 s6">
                    <input id="curp_derecho" type="text" data-length="18">
                    <label for="curp_derecho">CURP</label>
                </div>

                <div class="input-field col s12 s6">
                    <input id="puesto" type="text" class="validate">
                    <label for="puesto">Nombre de la plaza o puesto</label>
                </div>

                <div class="input-field col s12 s6">
                    <input id="sueldo" type="text" class="validate">
                    <label for="sueldo">Sueldo mensual</label>
                </div>

                <div class="input-field col s12 s6">
                    <input id="numero_empleado" type="text" class="validate">
                    <label for="numero_empleado">Numero de empleado</label>
                </div>

                <div class="input-field col s12 s6">
                    <select>
                        <option value="" disabled selected>Seleccione Adscripcion</option>
                        <option value="1">cet</option>
                        <option value="2">cecyt 1</option>
                        <option value="3">cecyt 2</option>
                    </select>
                    <label>Adscripcion</label>
                </div>

                <div class="input-field col s12 s6">
                    <select>
                        <option value="" disabled selected>Seleccione horario</option>
                        <option value="1">07:00 a 15:00</option>
                        <option value="2">08:00 a 15:00</option>
                        <option value="3">07:00 a 14:00</option>
                    </select>
                    <label>Horario de trabajo</label>
                </div>

                <div class="input-field col s6">
                    <input id="extension" type="text" data-length="5">
                    <label for="extension">Extension</label>
                </div>
            </div>
        </fieldset>
    </div>
    <div id="tabla4">
        <div class="card blue lighten-5 z-depth-3">
        <fieldset>
            <legend><h6>DATOS DEL CÓNYUGE (PADRE, MADRE):</h6></legend>
            <div class="row">
                <!-- Switch -->
                <label for="tieneconyuge">Tiene Conyuge</label>
                <div id="tieneconyuge" name="tieneconyuge" class="switch">
                    <label>
                        No
                        <input id="tienec" type="checkbox">
                        <span class="lever"></span>
                        Sí
                    </label>
                </div>

            </div>
            <div class="row" id="fila-conyuge">
                <div class="input-field col s6">
                    <input id="primer_apellido_conyuge" type="text" class="validate">
                    <label for="primer_apellido_conyuge">Primer Apellido</label>
                </div>
                <div class="input-field col s6">
                    <input id="segundo_apellido_conyuge" type="text" class="validate">
                    <label for="segundo_apellido_conyuge">Segundo Apellido</label>
                </div>
                <div class="input-field col s6">
                    <input id="nombre_conyuge" type="text" class="validate">
                    <label for="nombre_conyuge">Nombre(s)</label>
                </div>
                <div class="input-field col s12">
                    <input id="domicilio_conyuge" type="text" class="validate">
                    <label for="domicilio_conyuge">Domicilio particular (Calle, no. Ext., no. Int., Colonia,
                        Alcaldía o
                        municipio, Entidad federativa, C.P.</label>
                </div>
                <div class="input-field col s6">
                    <input id="telefono_fijo_conyuge" type="text" class="validate">
                    <label for="telefono_fijo_conyuge">Telefono Fijo</label>
                </div>
                <div class="input-field col s6">
                    <input id="telefono_celular_conyuge" type="text" class="validate">
                    <label for="telefono_celular_conyuge">Telefono celular</label>
                </div>
                <div class="input-field col s6">
                    <input id="lugar_trabajo_conyuge" type="text" class="validate">
                    <label for="lugar_trabajo_conyuge">Lugar de trabajo</label>
                </div>
                <div class="input-field col s6">
                    <input id="domicilio_trabajo_conyuge" type="text" class="validate">
                    <label for="domicilio_trabajo_conyuge">Domicilio del trabajo</label>
                </div>
                <div class="input-field col s6">
                    <input id="telefono_trabajo_conyuge" type="text" class="validate">
                    <label for="telefono_trabajo_conyuge">Telefono del trabajo</label>
                </div>
                <div class="input-field col s6">
                    <input id="extension_conyuge" type="text" class="validate">
                    <label for="extension_conyuge">Extension</label>
                </div>
            </div>
            </div>
        </fieldset>
    </div>
    </div>
    </div>
        <div class="row">
            <div id="letras2">
            <a id="btn-reset" class="z-depth-3 waves-effect waves-light btn">Limpiar</a>
            <button class="z-depth-3 btn waves-effect waves-light" type="submit" name="action">Enviar
                <i class="material-icons right">send</i>
            </button>
        </div>
        </div>
    </form>

    <footer id="futer"></footer>
</div>
</div>
</body>

</html>
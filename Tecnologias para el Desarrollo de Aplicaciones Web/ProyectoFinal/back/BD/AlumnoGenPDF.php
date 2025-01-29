<?php
    require("../BD/conexionBD.php");

    $folio=$_REQUEST['folio'];

    
    $sqlConyuge="select * from conyuge";//declarar consulta
    $respCon=mysqli_query($conexion,$sqlConyuge);//hacer consulta
    while($fila = mysqli_fetch_array($respCon)){
        if ( $fila['Folio'] == $folio ) {
            $primer_apellido_conyuge = $fila["Primer_Apellido_Conyuge"];
            $segundo_apellido_conyuge = $fila["Segundo_Apellido_Conyuge"];
            $nombre_conyuge = $fila["Nombre_Conyuge"];
            $calle_conyuge = $fila['calle_conyuge'];
            $noExt_conyuge = $fila['noExt_conyuge'];
            $noInt_conyuge = $fila['noInt_conyuge'];
            $colonia_conyuge = $fila['colonia_conyuge'];
            $alcaldia_conyuge = $fila['alcaldia_conyuge'];
            $entidad_conyuge = $fila['entidad_conyuge'];
            $cp_conyuge = $fila['cp_conyuge'];
            $telefono_fijo_conyuge = $fila["Telefono_Fijo_Conyuge"];
            $telefono_celular_conyuge = $fila["Telefono_Celular_Conyuge"];
            $lugar_trabajo_conyuge = $fila["Lugar_Trabajo_Conyuge"];
            $domicilio_trabajo_conyuge = $fila["Domicilio_Trabajo_Conyuge"];
            $telefono_trabajo_conyuge = $fila["Telefono_Trabajo_Conyuge"];
            $extension_conyuge = $fila["Extension"];
            $foto_conyuge = $fila["Imagen_Conyuge"];
            $tieneconyuge='si';
            break;
        }
    }

    $sqlDerecho="select * from datos_derecho";//derecho
    $respDerecho = mysqli_query($conexion,$sqlDerecho);
    while($fila = mysqli_fetch_array($respDerecho)){
        if ( $fila['Folio'] == $folio ) {
            $primer_apellido_derecho = $fila["Primer_Apellido_Derecho"];
            $segundo_apellido_derecho = $fila["Segundo_Apellido_Derecho"];
            $nombre_derecho = $fila["Nombre_Derecho"];
            $calle = $fila['calle'];
            $noExt = $fila['noExt'];
            $noInt = $fila['noInt'];
            $colonia= $fila['colonia'];
            $alcaldia= $fila['alcaldia'];
            $entidad = $fila['entidad'];
            $cp = $fila['cp'];
            $telefono_fijo = $fila["Telefono_Fijo_Derecho"];
            $telefono_celular = $fila["Telefono_Celular_Derecho"];
            $email_derecho = $fila["Email_Derecho"];
            $ocupacion = $fila["Ocupacion_Derecho"];
            $curp_derecho = $fila["Curp_Derecho"];
            $puesto = $fila["Puesto"];
            $sueldo = $fila["Sueldo"];
            $numero_empleado = $fila["Numero_Empleado"];
            $adscripcion = $fila["Adscripcion"];
            $horario = $fila["Horario_Trabajo"];
            $extension = $fila["Extension"];
            $foto_derecho = $fila["Imagen_Derecho"];
            $encontrado=1;
            break;
        }
    }

    $sqlGen="select * from datos_generales";//generales
    $respGen = mysqli_query($conexion,$sqlGen);
    while($fila = mysqli_fetch_array($respGen)){
        if ( $fila['Folio'] == $folio ) {
            $cendi = $fila["Cendi"];
            $grupo = $fila["Grupo"];
            $foto_autorizada = $fila["Imagen_Autorizada"];
            $cita = $fila["Cita"];
            $docs = $fila["Docs"];
            $fecha_r = date_parse($fila["FechaR"]);
            $encontrado=1;
            break;
        }
    }
    $sqlNin="select * from datos_niño";//niño
    $respNin = mysqli_query($conexion,$sqlNin);
    while($fila = mysqli_fetch_array($respNin)){
        if ( $fila['Folio'] == $folio ) {
            $primer_apellido = $fila["Primer_Apellido"];
            $segundo_apellido = $fila["Segundo_Apellido"];
            $nombre = $fila["Nombre"];    
            $fechaNac = $fila["FechaNac"];
            $email = $fila["Email"];    
            $edadAnios = $fila["Edad_Anios"];
            $edadMeses = $fila["Edad_Meses"];
            $curp = $fila["Curp"];   
            $foto = $fila["Imagen_Ninio"]; 
            $encontrado=1;
            break;
        }
    }
   
    mysqli_close($conexion);
?>
<?php
     include("../BD/AlumnoGenPDF.php");

     $meses = array("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre");
    //Datos generales

    if($grupo == "Lac I-II"){
        $tramite = "INSCRIPCION";
    } else{
        $tramite = "REINSCRIPCION";
    }
   

    $startYear = 2021;
    $endYear = 2022;
    $cendi = $cendi;

      //Registro
    $diaRegistro = $fecha_r["day"];
    $mesRegistro = $meses[$fecha_r["month"]-1];
    $anioRegistro = $fecha_r["year"];

   
    $grupo = $grupo;
    $aFoto = $foto_autorizada;

    if($cita == "no")
    {
        $cita = "N/A";
    }
 
    $docs = $docs;
    $fechaR = $fecha_r;



    //Datos del niño o niña
    $nNombre = $nombre;
    $nApellido1 = $primer_apellido;
    $nApellido2 = $segundo_apellido;
    $nFechaNacimiento = $fechaNac;
    $nEdadAnios = $edadAnios;
    $nEdadMeses = $edadMeses;
    $nCurp = $curp;
    $nFoto = $foto;


    //Datos del o la derechohabiente
    $dFoto = $foto_derecho;
    $dNombre = $nombre_derecho;
    $dApellido1 = $primer_apellido_derecho;
    $dApellido2 = $segundo_apellido_derecho;
    $dCalle = $calle;
    $dNumExt = $noExt;
    $dNumInt = $noInt;
    $dColonia = $colonia;
    $dAlcaldia = $alcaldia;
    $dEntidad = $entidad;
    $dCP = $cp;
    $dTelefono = $telefono_fijo;
    $dCelular = $telefono_celular;
    $dCorreo = $email_derecho;
    $dOcupacion = $ocupacion;
    $dCURP = $curp_derecho;
    $dPuesto = $puesto;
    $dSueldo = $sueldo;
    $dNumEmpleado = $numero_empleado;
    $dAdscripcion = $adscripcion;
    $dHorario = $horario;
    $dExtension = $extension;



    //Datos del conyuge
    $cFoto = $foto_conyuge;
    $cNombre = $nombre_conyuge;
    $cApellido1 = $primer_apellido_conyuge;
    $cApellido2 = $segundo_apellido_conyuge;
    $cCalle = $calle_conyuge;
    $cNumExt = $noExt_conyuge;
    $cNumInt = $noInt_conyuge;
    $cColonia = $colonia_conyuge;
    $cAlcaldia = $alcaldia_conyuge;
    $cEntidad = $entidad_conyuge;
    $cCP = $cp_conyuge;
    $cTelefono = $telefono_fijo_conyuge;
    $cCelular = $telefono_celular_conyuge;
    $cLugarTrabajo = $lugar_trabajo_conyuge;
    $cDomicilioTrabajo = $domicilio_trabajo_conyuge;
    $cTelefonoTrabajo = $telefono_trabajo_conyuge;
    $cExtension = $extension_conyuge;
    

  

    //include

?>
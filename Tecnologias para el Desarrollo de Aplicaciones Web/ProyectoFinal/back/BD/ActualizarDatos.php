<?php
    require("./conexionBD.php");

//Datos Generales

    $cendi="Amalia Solórzano de Cárdenas";//No se puede cambiar
    $folio=$_REQUEST['folio'];
    $grupo=$_REQUEST['grupo'];//
    //$foto_autorizada=$_REQUEST['foto_autorizada'];
    $foto_autorizada='1';

//Datos niño
    $primer_apellido=$_REQUEST['primer_apellido'];
    $segundo_apellido=$_REQUEST['segundo_apellido'];
    $nombre=$_REQUEST['nombre'];
    $fecha=$_REQUEST['fecha'];
    $edadAnios=$_REQUEST['edadAnios'];
    $edadMeses=$_REQUEST['edadMeses'];
    $email=$_REQUEST['email'];
    $curp=$_REQUEST['curp'];
    //$foto=$_REQUEST['foto'];
    $foto='2';

//Datos Derechoabiente
    $primer_apellido_derecho=$_REQUEST['primer_apellido_derecho'];
    $segundo_apellido_derecho=$_REQUEST['segundo_apellido_derecho'];
    $nombre_derecho=$_REQUEST['nombre_derecho'];
    $calle=$_REQUEST['calle'];
    $noExt=$_REQUEST['noExt'];
    $noInt = $_REQUEST['noInt'];
    $colonia= $_REQUEST['colonia'];
    $alcaldia= $_REQUEST['alcaldia'];
    $entidad = $_REQUEST['entidad'];
    $cp = $_REQUEST['cp'];
    $telefono_fijo=$_REQUEST['telefono_fijo'];
    $telefono_celular=$_REQUEST['telefono_celular'];
    $email_derecho=$_REQUEST['email_derecho'];
    $ocupacion=$_REQUEST['ocupacion'];
    $curp_derecho=$_REQUEST['curp_derecho'];
    $puesto=$_REQUEST['puesto'];
    $sueldo=$_REQUEST['sueldo'];
    $numero_empleado=$_REQUEST['numero_empleado'];
    $adscripcion=$_REQUEST['adscripcion'];
    $horario=$_REQUEST['horario'];
    $extension=$_REQUEST['extension'];
    //$foto_derecho=$_REQUEST['foto_derecho'];
    $foto_derecho='1';

//Datos Conyugue

    $primer_apellido_conyuge = $_REQUEST['primer_apellido_conyuge'];
    $segundo_apellido_conyuge = $_REQUEST['segundo_apellido_conyuge'];
    $nombre_conyuge = $_REQUEST['nombre_conyuge'];
    $calle_conyuge = $_REQUEST['calle_conyuge'];
    $noExt_conyuge = $_REQUEST['noExt_conyuge'];
    $noInt_conyuge = $_REQUEST['noInt_conyuge'];
    $colonia_conyuge = $_REQUEST['colonia_conyuge'];
    $alcaldia_conyuge = $_REQUEST['alcaldia_conyuge'];
    $entidad_conyuge = $_REQUEST['entidad_conyuge'];
    $cp_conyuge = $_REQUEST['cp_conyuge'];
    $telefono_fijo_conyuge=$_REQUEST['telefono_fijo_conyuge'];
    $telefono_celular_conyuge=$_REQUEST['telefono_celular_conyuge'];
    $lugar_trabajo_conyuge=$_REQUEST['lugar_trabajo_conyuge'];
    $domicilio_trabajo_conyuge=$_REQUEST['domicilio_trabajo_conyuge'];
    $telefono_trabajo_conyuge=$_REQUEST['telefono_trabajo_conyuge'];
    $extension_conyuge=$_REQUEST['extension_conyuge'];
    //$foto_conyuge=$_REQUEST['foto_conyuge'];
    $foto_conyuge='3';

    if ($primer_apellido_conyuge==''){
        $tieneconyuge='no';
    }else{
        $tieneconyuge='si';
    }

//Insertar los datos a BD


    $sqlActGeneral="update datos_generales set Cendi='$cendi',Grupo='$grupo',Imagen_Autorizada='$foto_autorizada' where folio = '$folio'";
   
    $sqlActNinio="update datos_niño set Primer_Apellido='$primer_apellido',Segundo_Apellido='$segundo_apellido',Nombre='$nombre',FechaNac='$fecha',Email='$email',Edad_Anios='$edadAnios',Edad_Meses='$edadMeses'
    ,Curp='$curp',Imagen_Ninio='$foto' where Folio='$folio'";
    
    $sqlActDerecho="update datos_derecho set Primer_Apellido_Derecho='$primer_apellido_derecho',Segundo_Apellido_Derecho='$segundo_apellido_derecho',Nombre_Derecho='".$nombre_derecho."',calle='"
    .$calle."',NoExt='".$noExt."',noInt='".$noInt."',colonia='".$colonia."',alcaldia='".$alcaldia."',entidad='".$entidad."',cp='".$cp."',Telefono_Fijo_Derecho='".$telefono_fijo."',Telefono_Celular_Derecho='"
    .$telefono_celular."',Email_Derecho='".$email_derecho."',Ocupacion_Derecho='".$ocupacion."',Curp_Derecho='".$curp_derecho."',Puesto='".$puesto."',Sueldo='".$sueldo."',Numero_Empleado='".$numero_empleado.
    "',Adscripcion='".$adscripcion."',Horario_Trabajo='".$horario."',Extension='".$extension."',Imagen_Derecho='".$foto_derecho."' where Folio='".$folio."'";
    
    if ($tieneconyuge=='si'){
        $sqlActConyuge="update conyuge set Primer_Apellido_Conyuge = '".$primer_apellido_conyuge."',Segundo_Apellido_Conyuge='".$segundo_apellido_conyuge."',Nombre_Conyuge='".$nombre_conyuge."',calle_conyuge='"
        .$calle_conyuge."',NoExt_conyuge='".$noExt_conyuge."',noInt_conyuge='".$noInt_conyuge."',colonia_conyuge='".$colonia_conyuge."',alcaldia_conyuge='".$alcaldia_conyuge."',entidad_conyuge='".$entidad_conyuge.
        "',cp_conyuge='".$cp_conyuge."',Telefono_Fijo_Conyuge='".$telefono_fijo_conyuge."',Telefono_Celular_Conyuge='".$telefono_celular_conyuge."',Lugar_Trabajo_Conyuge='".$lugar_trabajo_conyuge."',Domicilio_Trabajo_Conyuge='"
        .$domicilio_trabajo_conyuge."',Telefono_Trabajo_Conyuge='".$telefono_trabajo_conyuge."',Extension='".$extension_conyuge."',Imagen_Conyuge='".$foto_conyuge."' where Folio='".$folio."'";
        mysqli_query($conexion,$sqlActConyuge);
    }
    
    mysqli_query($conexion,$sqlActNinio);
    mysqli_query($conexion,$sqlActGeneral);
    mysqli_query($conexion,$sqlActDerecho);

    mysqli_close($conexion);//Cerrar conexion con BD
    header("location: ../../front/admin.php")
?>  
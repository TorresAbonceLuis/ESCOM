<?php
//sacar todos los datos de la BD para el admin

    require("./conexionBD.php");

    //datos generales
    $result=array();
    //declarar consulta
    $sqlGeneral=
        "SELECT DISTINCT datos_generales.Folio, Cendi, Grupo, Imagen_Autorizada, datos_niño.Primer_Apellido, datos_niño.Segundo_Apellido, datos_niño.Nombre, datos_niño.FechaNac, datos_niño.Email,datos_niño.Edad_Anios,datos_niño.Edad_Meses,datos_niño.Curp,datos_niño.Imagen_Ninio,datos_derecho.Primer_Apellido_Derecho,datos_derecho.Segundo_Apellido_Derecho,datos_derecho.Nombre_Derecho,datos_derecho.calle,datos_derecho.noExt,datos_derecho.noInt,datos_derecho.colonia,datos_derecho.alcaldia,datos_derecho.entidad,datos_derecho.cp,datos_derecho.Telefono_Fijo_Derecho,datos_derecho.Telefono_Celular_Derecho,datos_derecho.Email_Derecho,datos_derecho.Ocupacion_Derecho,datos_derecho.Curp_Derecho,datos_derecho.Puesto,datos_derecho.Sueldo,datos_derecho.Numero_Empleado,datos_derecho.Adscripcion,datos_derecho.Horario_Trabajo,datos_derecho.Extension,datos_derecho.Imagen_Derecho,conyuge.Primer_Apellido_Conyuge,conyuge.Segundo_Apellido_Conyuge,conyuge.Nombre_Conyuge,conyuge.Nombre_Conyuge,conyuge.calle_conyuge,conyuge.noExt_conyuge,conyuge.noInt_conyuge,conyuge.colonia_conyuge,conyuge.alcaldia_conyuge,conyuge.entidad_conyuge,conyuge.cp_conyuge,conyuge.Telefono_Fijo_Conyuge,conyuge.Telefono_Celular_Conyuge,conyuge.Lugar_Trabajo_Conyuge,conyuge.Domicilio_Trabajo_Conyuge,conyuge.Telefono_Trabajo_Conyuge,conyuge.Extension,conyuge.Imagen_Conyuge
        from datos_generales 
        INNER JOIN datos_niño on datos_niño.Folio = datos_generales.Folio
        INNER JOIN datos_derecho on datos_derecho.Folio = datos_generales.Folio
        RIGHT JOIN conyuge on conyuge.Folio = datos_generales.Folio
        UNION
        SELECT DISTINCT datos_generales.Folio, Cendi, Grupo, Imagen_Autorizada, datos_niño.Primer_Apellido, datos_niño.Segundo_Apellido, datos_niño.Nombre, datos_niño.FechaNac, datos_niño.Email,datos_niño.Edad_Anios,datos_niño.Edad_Meses,datos_niño.Curp,datos_niño.Imagen_Ninio,datos_derecho.Primer_Apellido_Derecho,datos_derecho.Segundo_Apellido_Derecho,datos_derecho.Nombre_Derecho,datos_derecho.calle,datos_derecho.noExt,datos_derecho.noInt,datos_derecho.colonia,datos_derecho.alcaldia,datos_derecho.entidad,datos_derecho.cp,datos_derecho.Telefono_Fijo_Derecho,datos_derecho.Telefono_Celular_Derecho,datos_derecho.Email_Derecho,datos_derecho.Ocupacion_Derecho,datos_derecho.Curp_Derecho,datos_derecho.Puesto,datos_derecho.Sueldo,datos_derecho.Numero_Empleado,datos_derecho.Adscripcion,datos_derecho.Horario_Trabajo,datos_derecho.Extension,datos_derecho.Imagen_Derecho,conyuge.Primer_Apellido_Conyuge,conyuge.Segundo_Apellido_Conyuge,conyuge.Nombre_Conyuge,conyuge.Nombre_Conyuge,conyuge.calle_conyuge,conyuge.noExt_conyuge,conyuge.noInt_conyuge,conyuge.colonia_conyuge,conyuge.alcaldia_conyuge,conyuge.entidad_conyuge,conyuge.cp_conyuge,conyuge.Telefono_Fijo_Conyuge,conyuge.Telefono_Celular_Conyuge,conyuge.Lugar_Trabajo_Conyuge,conyuge.Domicilio_Trabajo_Conyuge,conyuge.Telefono_Trabajo_Conyuge,conyuge.Extension,conyuge.Imagen_Conyuge
        from datos_generales 
        INNER JOIN datos_niño on datos_niño.Folio = datos_generales.Folio
        INNER JOIN datos_derecho on datos_derecho.Folio = datos_generales.Folio
        LEFT JOIN conyuge on conyuge.Folio = datos_generales.Folio
        ORDER by Grupo";

    $respGen=mysqli_query($conexion,$sqlGeneral);//hacer consulta
    while($filaGen=mysqli_fetch_assoc($respGen)){
        $result[]=$filaGen;
    }

    $resultado=json_encode($result);
    echo $resultado;
    mysqli_close($conexion);

<?php
    require("./conexionBD.php");
    $folioBorrar = $_REQUEST['folioBorrar'];
    $sqlBorarDerecho="delete from datos_derecho where folio = '".$folioBorrar."'";
    mysqli_query($conexion,$sqlBorarDerecho);

    $sqlBorarConyuge="delete from conyuge where folio = '".$folioBorrar."'";
    mysqli_query($conexion,$sqlBorarConyuge);

    $sqlBorarNiño="delete from datos_niño where folio = '".$folioBorrar."'";
    mysqli_query($conexion,$sqlBorarNiño);

    $sqlGrupo="select grupo from datos_generales where folio = '".$folioBorrar."'";
    $respuesta=mysqli_query($conexion,$sqlGrupo);
    $Grupo=mysqli_fetch_row($respuesta);

    $sqlLugares="select lugares from horario where grupo = '".$Grupo[0]."'";
    $respuesta2=mysqli_query($conexion,$sqlLugares);
    $lugares=mysqli_fetch_row($respuesta2);
    $lugares[0]-=1;
    $sqlLugares2 = "update horario set lugares = ".$lugares[0]." where grupo = '".$Grupo[0]."'";
    mysqli_query($conexion,$sqlLugares2);

    $sqlBorarGeneral="delete from datos_generales where folio = '".$folioBorrar."'";
    mysqli_query($conexion,$sqlBorarGeneral);
    mysqli_close($conexion);

?>
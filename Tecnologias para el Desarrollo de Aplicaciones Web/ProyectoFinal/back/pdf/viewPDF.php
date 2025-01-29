<?php

include("generatePDF.php");

global $pdf;
$pdf ->Output("Ficha de Registro ".$folio.".pdf","I");

?>

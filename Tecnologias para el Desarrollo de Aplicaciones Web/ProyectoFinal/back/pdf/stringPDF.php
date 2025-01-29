<?php

include("generatePDF.php");

global $pdf;
$pdfDoc = $pdf ->Output("","S");

?>

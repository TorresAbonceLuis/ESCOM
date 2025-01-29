<?php
ob_start();
    /* Clase fpdf */
    include("style.php");
    
    include("requestData.php");
   
    require("./tfpdf/tfpdf.php");

    class PDF extends tFPDF
    {
        function getBodyWidth(){
            return $this->GetPageWidth() - $this->lMargin - $this->rMargin;
        }

        // Cabecera de página
        function Header(){
            // Logo
            $this->Image('../assets/SEP_IPN.png',$this->lMargin,8,120);
            $this->Ln(20);  
        }

        // Pie de página
        function Footer(){
            // Posición: a 1.5 cm del final
            $this->SetY(-23);
            // Arial italic 8
            $this->SetFont("DejaVu-Serif","",6.5);

            $this->Image('../assets/pleca_flores_magon.png',$this->lMargin,$this->GetPageHeight()-25,$this->getBodyWidth());

          $this->MultiCell(0,3, 
          "Juan de Dios Bátiz esquina Miguel Othón de Mendizábal, Col. Nueva Industrial Vallejo, Alcaldía Gustavo A. Madero 07738 \nCiudad de México. Tel. 5729-6000, 5729-6300 Ext. 57701, 57702, 57704. Correo electrónico: cocendi@ipn.mx",
           0, 'L', false);
        }
    }

    $pdf = new PDF("P","mm","Letter");
    //  $pdf->Error("Ha ocurrido un error al generar el PDF");
    $pdf->AliasNbPages();
    $pdf->AddPage();

    $gris = 230;

    //Establecemos los margenes 
    $margins = 15;
    $pdf->SetMargins($margins, $margins);
    $pdf->SetAutoPageBreak(true);
    $pdf->SetLineWidth(0.1);
    
    function getFrac($numerator, $denominator){
        global $pdf;
        return $pdf->getBodyWidth() / $denominator * $numerator;
    }

    $pdf->SetFillColor(220,230,240 );
    $pdf->AddFont('Arial','','arial.ttf',true);
    $pdf->AddFont('DejaVu-Serif','','DejaVuSerif.ttf',true);
    $pdf->AddFont('Arial','B','arialbd.ttf',true);


    $pdf->SetFont('Arial','B',$titleFontSize);

    //ENCABEZADO
    $pdf->Ln(1);
    $pdf->Cell(0,$lineHeight+2,"FICHA DE ".$tramite,0,1,"C");
    $pdf->Cell(0,$lineHeight+2,"CICLO ESCOLAR: ". $startYear ." - ". $endYear ,0,1,"C");
    $pdf->Cell(0,$lineHeight+2,"CENDI: ". $cendi ,0,1,"C");

    //FOTO, FOLIO, GRUPO
    $pdf->SetXY(getFrac(1,12)*11, 30);
    $pdf->Cell(25,30,"Foto", 1, 1, 'C');
    $pdf->Image($nFoto,getFrac(11,12),30,25,30, 'JPG');   //Foto del ninno
    $pdf->SetXY(getFrac(5,7)+$margins, 63);
    $pdf->Cell(getFrac(2,21),$lineHeight,"Folio:", 1, 0, 'C'); 
    $pdf->Cell(getFrac(4,21),$lineHeight,$folio, 1, 1, 'L', true);
    $pdf->SetXY(getFrac(1,7)*5+$margins, 63+ $lineHeight); #
    $pdf->Cell(getFrac(2,21),$lineHeight,"Grupo:", 1, 0, 'C');
    $pdf->Cell(getFrac(4,21),$lineHeight,$grupo, 1, 1, 'L', true); #
    $pdf->Ln(5);
  
    //DATOS DEL NIÑO O NIÑA
    $pdf->Cell(0,$lineHeight,"DATOS DE LA NIÑA O EL NIÑO:",0,1,"L");
    $pdf->SetFont('Arial','',$fontSize);
    
    //1ra Linea - Nombre completo
    $pdf->Cell(getFrac(1,3),$lineHeight,$nApellido1,1,0,"C",true); #
    $pdf->Cell(getFrac(1,3),$lineHeight,$nApellido2,1,0,"C",true); #
    $pdf->Cell(getFrac(1,3),$lineHeight,$nNombre,1,1,"C",true); #
    $pdf->Cell(getFrac(1,3),$lineHeight,"Primer Apellido",1,0,"C"); 
    $pdf->Cell(getFrac(1,3),$lineHeight,"Segundo Apellido",1,0,"C");
    $pdf->Cell(getFrac(1,3),$lineHeight,"Nombre(s)",1,1,"C");

    //2da Linea - Fecha de nacimiento
    $pdf->Cell(getFrac(4,16),$lineHeight,"Fecha de Nacimiento:",1,0,"C");
   // $pdf->Cell(getFrac(1,16),$lineHeight,"Día",1,0,"C");
    $pdf->Cell(getFrac(6,16),$lineHeight,$nFechaNacimiento,1,0,"C", true);
   // $pdf->Cell(getFrac(1,16),$lineHeight,"Mes",1,0,"C");
   // $pdf->Cell(getFrac(2,16),$lineHeight,"Diciembre",1,0,"C", true);
    //$pdf->Cell(getFrac(1,16),$lineHeight,"Año",1,0,"C");
   // $pdf->Cell(getFrac(1,16),$lineHeight,"",1,0,"C", true);
    $pdf->Cell(getFrac(2,16),$lineHeight,"Edad:",1,0,"C");
    $pdf->Cell(getFrac(1,16),$lineHeight,"Años",1,0,"C");
    $pdf->Cell(getFrac(1,16),$lineHeight,$nEdadAnios,1,0,"C", true); #
    $pdf->Cell(getFrac(1,16),$lineHeight,"Mes",1,0,"C");
    $pdf->Cell(getFrac(1,16),$lineHeight,$nEdadMeses,1,1,"C", true); #

    //3ra Linea - Curp
    $pdf->Cell(getFrac(2,12),$lineHeight,"CURP:",1,0,"C");
    $pdf->Cell(getFrac(4,12),$lineHeight,$nCurp,1,0,"C",true); #


    $pdf->Ln(8);
    // ### DERECHOHABIENTE
    //1ra Linea - Nombre completo
    $pdf->SetFont('Arial','B',$titleFontSize);
    $pdf->Cell(0,$lineHeight,"DATOS DEL O LA DERECHOHABIENTE:",0,1,"L");
    $pdf->SetFont('Arial','',$fontSize);
    $pdf->Cell(getFrac(1,3),$lineHeight,$dApellido1,1,0,"C",true); #
    $pdf->Cell(getFrac(1,3),$lineHeight,$dApellido1,1,0,"C",true);  #
    $pdf->Cell(getFrac(1,3),$lineHeight,$dNombre,1,1,"C",true); #
    $pdf->Cell(getFrac(1,3),$lineHeight,"Primer Apellido",1,0,"C"); 
    $pdf->Cell(getFrac(1,3),$lineHeight,"Segundo Apellido",1,0,"C");
    $pdf->Cell(getFrac(1,3),$lineHeight,"Nombre(s)",1,1,"C");

    //2da Linea -  Domicilio
    $x = $pdf->GetX();
    $y = $pdf->GetY();
    $pdf->MultiCell(getFrac(1,10),$lineHeight,"Domicilio particular:",1,"C");
   
    $pdf->SetXY($x+getFrac(1,10),$y); //Nos posicionamos delante del la celda anterior

    $pdf->Cell(getFrac(4,10),$lineHeight,$dCalle,1,0,"C",true); #
    $pdf->Cell(getFrac(1,10),$lineHeight,$dNumExt,1,0,"C",true); #
    $pdf->Cell(getFrac(1,10),$lineHeight,$dNumInt,1,0,"C",true); #
    $pdf->Cell(getFrac(3,10),$lineHeight,$dColonia,1,1,"C",true); #
    $x = $pdf->GetX();
    $y = $pdf->GetY();
    $pdf->SetXY($x+getFrac(1,10),$y); //Nos posicionamos delante del la celda anterior
    $pdf->Cell(getFrac(4,10),$lineHeight,"Calle",1,0,"C");
    $pdf->Cell(getFrac(1,10),$lineHeight,"N°. Ext.",1,0,"C");
    $pdf->Cell(getFrac(1,10),$lineHeight,"N°. Int.",1,0,"C");
    $pdf->Cell(getFrac(3,10),$lineHeight,"Colonia",1,1,"C");

    //3ra Linea - Alcaldía, Entidad Federativa, CP y Teléfono
    $pdf->Cell(getFrac(3,10),$lineHeight,$dAlcaldia,1,0,"C",true);
    $pdf->Cell(getFrac(2,10),$lineHeight,$dEntidad,1,0,"C",true);
    $pdf->Cell(getFrac(1,10),$lineHeight,$dCP,1,0,"C",true);
    $pdf->Cell(getFrac(2,10),$lineHeight,$dTelefono,1,0,"C",true);
    $pdf->Cell(getFrac(2,10),$lineHeight,$dCelular,1,1,"C",true);
    $pdf->Cell(getFrac(3,10),$lineHeight,"Alcaldía o municipio",1,0,"C");
    $pdf->Cell(getFrac(2,10),$lineHeight,"Entidad federativa",1,0,"C");
    $pdf->Cell(getFrac(1,10),$lineHeight,"C.P.",1,0,"C");
    $pdf->Cell(getFrac(2,10),$lineHeight,"Teléfono fijo",1,0,"C");
    $pdf->Cell(getFrac(2,10),$lineHeight,"Teléfono celular",1,1,"C");
    //4ta Linea - Correo electrónico, Ocupación y Curp
    $pdf->Cell(getFrac(1,3),$lineHeight,$dCorreo,1,0,"C",true); #
    $pdf->Cell(getFrac(1,3),$lineHeight,$dOcupacion,1,0,"C",true); #
    $pdf->Cell(getFrac(1,3),$lineHeight,$dCURP,1,1,"C",true); #

    $pdf->Cell(getFrac(1,3),$lineHeight,"Correo electrónico",1,0,"C");
    $pdf->Cell(getFrac(1,3),$lineHeight,"Ocupación",1,0,"C");
    $pdf->Cell(getFrac(1,3),$lineHeight,"CURP",1,1,"C");

    //5ta Linea - Puesto, Sueldo y No. de Empleado
    $pdf->Cell(getFrac(3,7),$lineHeight,$dPuesto,1,0,"C",true); #
    $pdf->Cell(getFrac(2,7),$lineHeight,$dSueldo,1,0,"C",true); #
    $pdf->Cell(getFrac(2,7),$lineHeight,$dNumEmpleado,1,1,"C",true); #
    $pdf->Cell(getFrac(3,7),$lineHeight,"Nombre de plaza o puesto",1,0,"C");
    $pdf->Cell(getFrac(2,7),$lineHeight,"Sueldo mensual",1,0,"C");
    $pdf->Cell(getFrac(2,7),$lineHeight,"Número de empleado",1,1,"C");
   
    //6ta Linea - Adscripción
    $pdf->Cell(getFrac(1,1),$lineHeight,$dAdscripcion,1,1,"C",true); #
    $pdf->Cell(getFrac(1,1),$lineHeight,"Adscripción (Secretaría, Coordinación, Dirección, Centro, Escuela, etc.) [Iniciales]",1,1,"C"); 
    
    

    //8va Linea - Horario de trabajo, Extensión
    $pdf->Cell(getFrac(3,4),$lineHeight,$dHorario,1,0,"C",true); #
    $pdf->Cell(getFrac(1,4),$lineHeight,$dExtension,1,1,"C",true); #
    $pdf->Cell(getFrac(3,4),$lineHeight,"Horario de trabajo",1,0,"C");
    $pdf->Cell(getFrac(1,4),$lineHeight,"Extensión",1,0,"C");

    $pdf->Ln(8);
    if ($tieneconyuge=='si'){
        // ### CONYUGE agregar opcion si tiene o no conyuge supongo con un if
        //1ra Linea - Nombre completo
        $pdf->SetFont('Arial','B',$titleFontSize);
        $pdf->Cell(0,$lineHeight,"DATOS DEL CONYUGE (PADRE, MADRE):",0,1,"L");
        $pdf->SetFont('Arial','',$fontSize);
        $pdf->Cell(getFrac(1,3),$lineHeight,$cApellido2,1,0,"C",true); #
        $pdf->Cell(getFrac(1,3),$lineHeight,$cApellido1,1,0,"C",true); #
        $pdf->Cell(getFrac(1,3),$lineHeight,$cNombre,1,1,"C",true); #
        $pdf->Cell(getFrac(1,3),$lineHeight,"Primer Apellido",1,0,"C"); 
        $pdf->Cell(getFrac(1,3),$lineHeight,"Segundo Apellido",1,0,"C");
        $pdf->Cell(getFrac(1,3),$lineHeight,"Nombre(s)",1,1,"C");
        

        //2da Linea - Domicilio Particular
        $x = $pdf->GetX();
        $y = $pdf->GetY();
        $pdf->MultiCell(getFrac(1,10),$lineHeight,"Domicilio particular:",1,"C");
    
        $pdf->SetXY($x+getFrac(1,10),$y); //Nos posicionamos delante del la celda anterior
        $pdf->Cell(getFrac(4,10),$lineHeight,$cCalle,1,0,"C",true); #
        $pdf->Cell(getFrac(1,10),$lineHeight,$cNumExt,1,0,"C",true); #
        $pdf->Cell(getFrac(1,10),$lineHeight,$cNumInt,1,0,"C",true); #
        $pdf->Cell(getFrac(3,10),$lineHeight,$cColonia,1,1,"C",true); #
        $x = $pdf->GetX();
        $y = $pdf->GetY();
        $pdf->SetXY($x+getFrac(1,10),$y); //Nos posicionamos delante del la celda anterior
        $pdf->Cell(getFrac(4,10),$lineHeight,"Calle",1,0,"C");
        $pdf->Cell(getFrac(1,10),$lineHeight,"N°. Ext.",1,0,"C");
        $pdf->Cell(getFrac(1,10),$lineHeight,"N°. Int.",1,0,"C");
        $pdf->Cell(getFrac(3,10),$lineHeight,"Colonia",1,1,"C");

        //3ra Linea - Alcaldía, Entidad Federativa, CP y Teléfono
        $pdf->Cell(getFrac(3,10),$lineHeight,$cAlcaldia,1,0,"C",true);
        $pdf->Cell(getFrac(2,10),$lineHeight,$cEntidad,1,0,"C",true);
        $pdf->Cell(getFrac(1,10),$lineHeight,$cCP,1,0,"C",true);
        $pdf->Cell(getFrac(2,10),$lineHeight,$cTelefono,1,0,"C",true);
        $pdf->Cell(getFrac(2,10),$lineHeight,$cCelular,1,1,"C",true);
        $pdf->Cell(getFrac(3,10),$lineHeight,"Alcaldía o municipio",1,0,"C");
        $pdf->Cell(getFrac(2,10),$lineHeight,"Entidad federativa",1,0,"C");
        $pdf->Cell(getFrac(1,10),$lineHeight,"C.P.",1,0,"C");
        $pdf->Cell(getFrac(2,10),$lineHeight,"Teléfono fijo",1,0,"C");
        $pdf->Cell(getFrac(2,10),$lineHeight,"Teléfono celular",1,1,"C");

        //4ta Linea - Lugar de trabajo, Ocupación
        $pdf->Cell(getFrac(1,4),$lineHeight,"Lugar de trabajo:",1,0,"L");
        $pdf->Cell(getFrac(3,4),$lineHeight,$cLugarTrabajo,1,1,"C",true);
        //$pdf->Cell(getFrac(1,5),$lineHeight,"Ocupación:",1,0,"C");
        //$pdf->Cell(getFrac(1,5),$lineHeight,"",1,1,"C",true);

        //5ta Linea - Domicilio del trabajo
        $pdf->Cell(getFrac(1,4),$lineHeight,"Domicilio del trabajo:",1,0,"L");
        $pdf->Cell(getFrac(3,4),$lineHeight,$cDomicilioTrabajo,1,1,"L",true);

        //6ta Linea - Teléfono del trabajo, Religión
        $pdf->Cell(getFrac(1,4),$lineHeight,"Teléfono del trabajo:",1,0,"L");
        $pdf->Cell(getFrac(1,4),$lineHeight,$cTelefonoTrabajo,1,0,"C",true);
        $pdf->Cell(getFrac(1,8),$lineHeight,"Extension:",1,0,"L");
        $pdf->Cell(getFrac(1,6),$lineHeight,$cExtension,1,1,"C",true);
        $x = $pdf->GetX();
        $y = $pdf->GetY();
        // falta extension
      
      //  $pdf->MultiCell(getFrac(1,4),$lineHeight*2,"Religión de la familia:",1,"C");
      //  $pdf->SetXY($x+getFrac(1,4),$y);
        // $pdf->Cell(getFrac(1,4),$lineHeight,"",1,1,"C",true);
      
    }

    $pdf->AddPage();

    $pdf->SetFont('Arial','B',7);
    $pdf-> Cell(0,$lineHeight,"FOTOGRAFÍAS DEL O LA DERECHOHABIENTE, CÓNYUGE (PADRE, MADRE) Y PERSONA AUTORIZADA PARA RECOGER AL NIÑO O LA NIÑA:",0,1,"C");

    $rectHeight = 30;
    $rectWidth = 25;
    
    $spaceBetween = ($pdf->getBodyWidth() - (getFrac(1,12)*4 + $rectWidth*3))/2 ; //Espacio entre cada rectangulo

    //FOTOS
    $pdf->SetXY($margins+ getFrac(2,12), 50);
    $pdf->Rect($pdf->GetX(), $pdf->GetY(), $rectWidth, $rectHeight);
    $pdf->Image($dFoto,$margins+ getFrac(2,12),50,25,30, 'JPG');
    $pdf->SetXY($pdf->GetX()+$rectWidth + $spaceBetween, $pdf->GetY());
    $pdf->Rect($pdf->GetX(), $pdf->GetY(), $rectWidth, $rectHeight);
    $pdf->Image($cFoto,$pdf->GetX(), $pdf->GetY(),25,30, 'JPG');
    $pdf->SetXY($pdf->GetX()+$rectWidth + $spaceBetween, $pdf->GetY());
    $pdf->Rect($pdf->GetX(), $pdf->GetY(), $rectWidth, $rectHeight);
    $pdf->Image($aFoto,$pdf->GetX(), $pdf->GetY(),25,30, 'JPG');

    $pdf->SetXY(35, $pdf->GetY()+$rectHeight+$lineHeight);

    $pdf->SetFont('Arial','B',$fontSize);
    $pdf->Cell(getFrac(1,4),$lineHeight,"DERECHOHABIENTE",0,0,"C");
    $pdf->Cell(3,$lineHeight,"",0,0,"C");
    $pdf->Cell(getFrac(1,4),$lineHeight,"CONYUGE",0,0,"C");
    $pdf->Cell(3,$lineHeight,"",0,0,"C");
    $pdf->Cell(getFrac(1,4),$lineHeight,"PERSONA AUTORIZADA",0,0,"C");

    $pdf->Ln(20);

    $pdf->Cell(getFrac(1,3),$lineHeight,"Fecha de entrevista:",1,0,"L");
    $pdf->Cell(getFrac(1,3),$lineHeight,$cita,1,1,"C",true);
    $pdf->Cell(getFrac(1,3),$lineHeight,"Fecha de entrega de documentos:",1,0,"L");
    $pdf->Cell(getFrac(1,3),$lineHeight,$docs,1,1,"C",true);

    $pdf->Ln(15);
   
    //FECHA DE REGISTRO
    $pdf->SetFont('Arial','B',$fontSize);
    $spaceAside = ($pdf->getBodyWidth() - ($pdf->GetStringWidth("Ciudad de México a ".$diaRegistro." de ".$mesRegistro." de ".$anioRegistro)+10)) / 2;
    $pdf->SetXY($spaceAside+$margins, $pdf->GetY()+$lineHeight);

    $pdf->SetFont('Arial','',$fontSize);
    $pdf->Cell($pdf->GetStringWidth("Ciudad de México a ")+2,$lineHeight,"Ciudad de México a ",0,0,"L");
    $pdf->SetFont('Arial','B',$fontSize);
    $pdf->Cell($pdf->GetStringWidth($diaRegistro)+2,$lineHeight,$diaRegistro,0,0,"L",true);
    $pdf->SetFont('Arial','',$fontSize);
    $pdf->Cell($pdf->GetStringWidth(" de ")+2,$lineHeight," de ",0,0,"L");
    $pdf->SetFont('Arial','B',$fontSize);
    $pdf->Cell($pdf->GetStringWidth($mesRegistro)+2,$lineHeight,$mesRegistro,0,0,"L",true);
    $pdf->SetFont('Arial','',$fontSize);
    $pdf->Cell($pdf->GetStringWidth(" de ")+2,$lineHeight," de ",0,0,"L");
    $pdf->SetFont('Arial','B',$fontSize);
    $pdf->Cell($pdf->GetStringWidth($anioRegistro)+2,$lineHeight,$anioRegistro,0,0,"L",true);



  
    $pdf->Ln(12);
    $pdf->SetXY($margins + getFrac(1,3), $pdf->GetY()+$lineHeight);
    $pdf->Cell(getFrac(1,3), 10, "", "B", 2, "C", true);
    $pdf->Cell(getFrac(1,3), 10, "Nombre y Firma del o la derechohabiente",0, 1, "C");


    $pdf->Output( "I", "Ficha de Registro ".$folio.".pdf");
    $pdfDoc = $pdf->Output("", "S");

    include ("../mail/sendMail.php");
ob_end_flush(); 
?>
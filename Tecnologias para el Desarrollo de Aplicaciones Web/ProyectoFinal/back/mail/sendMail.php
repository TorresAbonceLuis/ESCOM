<?php

use PHPMailer\PHPMailer\PHPMailer;

require 'phpMailer/Exception.php';
require 'phpMailer/PHPMailer.php';
require 'phpMailer/SMTP.php';

//include("../pdf/stringPDF.php");

$email_user = "equipo3tecweb@gmail.com"; //OJO. Debes actualizar esta línea con tu información
$email_password = "otlheyotnscyleep"; //OJO. Debes actualizar esta línea con tu información
$the_subject = "Registro CENDI";
$address_to = $email_derecho; //OJO. Debes actualizar esta línea con tu información
$from_name = "CENDI";
$mail = new PHPMailer();

// ---------- datos de la cuenta de Gmail -------------------------------
$mail->Username = $email_user;
$mail->Password = $email_password; 
//-----------------------------------------------------------------------
// $mail->SMTPDebug = 1;
$mail->SMTPSecure = 'ssl';
$mail->Host = "smtp.gmail.com"; // GMail
$mail->Port = 465;
$mail->IsSMTP(); // use SMTP
$mail->SMTPAuth = true;

$mail->setFrom($mail->Username,$from_name);
$mail->AddAddress($address_to); // recipients email

//Datos personales--------------------------------------------------------
 


//------------------------------------------------------------
$mail->Subject = $the_subject;
$mail->AddEmbeddedImage('../assets/banne-cendi-min.jpg', 'banner');


$mail->Body ='<img alt="Banner del cendi" src="cid:banner" style="width:100%">';
$mail->Body .="<h1 style='color:#3498db;'>Buen día, C. $nombre_derecho </h1>";
$mail->Body .= "<p>Usted ha concluido su registro exitosamente. A continuación adjutamos un archivo pdf con los datos registrados. Si usted no ha solicitado el registro, haga caso omiso a este correo.</p>";

global $pdfDoc;
$mail->Body .= "<p>Este correo es sólamente informativo, favor de no responer.</p>";

$mail->AddStringAttachment($pdfDoc, "Ficha de Registro $folio.pdf", $encoding = 'base64', $type = 'application/pdf');

$mail->IsHTML(true);
if(!$mail->Send()) {
    $message =  "El correo no se ha enviado. Mailer Error: " . $mail->ErrorInfo;
  } else {
    $message = "El correo se ha enviado correctamente";
  }

  echo "<script>alert('$message');</script>";

?>
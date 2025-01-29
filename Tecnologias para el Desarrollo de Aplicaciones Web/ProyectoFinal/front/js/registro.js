$(document).ready(function () {
    //Importaciones
    $("#navegacion").load("./compartidos/barranav.html");
    $("#futer").load("./compartidos/futer.html");

    $('#hola').hide();

    //Activaciones
   // $('select').formSelect(); //jala select
    // $('input#input_text, textarea#textarea2').characterCounter(); // jala counter
    // $('.datepicker').datepicker({
    //     format: 'dd mmm yyyy',
    //     yearRange: [anioHoy() - 6, anioHoy()],
    //     i18n: {
    //         months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    //         monthsShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
    //         weekdays: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
    //         weekdaysShort: ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'],
    //         weekdaysAbbrev: ['D', 'L', 'M', 'M', 'J', 'V', 'S'],
    //         selectMonths: true,
    //         selectYears: 100, // Puedes cambiarlo para mostrar más o menos años
    //         today: 'Hoy',
    //         clear: 'Limpiar',
    //         close: 'Ok',
    //     }
    //     ,
    //     onSelect: function (selDate) {
    //         var hoy = new Date();
    //         var fechaNac = new Date(selDate);
    //         var anios = hoy.getFullYear() - fechaNac.getFullYear();
    //         var meses = hoy.getMonth() - fechaNac.getMonth();
    //         if (anios <= 0 && meses <= 0 && (hoy.getDate() < fechaNac.getDate())) {
    //             let texto = "Esa criatura aún no ha nacido. " + "Años: " + anios + ", meses: " + meses;
    //             alert(texto);
    //         } else {
    //             if (meses < 0) {
    //                 anios--;
    //                 meses = (12 + meses);
    //             }
    //             if ((anios > 6) || (anios == 6 && meses > 0)) {
    //                 let texto = "Va para Primaria, no CENDI. " + "Años: " + anios + ", meses: " + meses;
    //                 alert(texto);
    //             } else {
    //                 //let texto = "Chido "+ "Años: " + anios + ", meses: " + meses;
    //                 //alert(texto);
    //             }
    //         }
    //         ///Se llenan los campos con la edad calculada
    //         $('#edadAnios').val(anios);
    //         $('#edadMeses').val(meses);
    //         M.updateTextFields();

    //     }
    // });
    var alumno = { curp: 'Jose Angel', folio: 'Espinosa' };
    //activaciones
    //$('.datepicker').datepicker();
   
      // Initialize Firebase
      

    
    $('#btn-imprimir').hide();
    $('#btn-imprimir').click(function(){
        let direc = "../back/pdf/generatePDF.php?folio="+alumno.folio;
        window.open(direc,'_blank');
    });
    
});
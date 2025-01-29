
function enviaJSON(informacion, actionUrl) {
    $.ajax({
        type: "POST",
        url: actionUrl,
        data: informacion, // envia el json
        success: function (data) {
            let jsonData = $.parseJSON(data);
            console.log(data);
            if (jsonData.state == 0 && jsonData.folio == alumno.folio) {

                Swal.fire({
                    title: 'Enviado!',
                    text: 'Tu datos han sido guardados.',
                    icon: 'success',
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'Generar PDF',
                }).then((result) => {
                    if (result.isConfirmed) {
                        let direc = "../back/pdf/generatePDF.php?folio=" + alumno.folio;
                        window.open(direc, '_blank');
                    }
                });
                $('#btn-imprimir').show();
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Error BD',
                    text: "Error",
                    showConfirmButton: true,
                });
            }
        }
    });
}

// const subirFoto = async (idFoto, actionUrl) => {
//     const file = $(idFoto).prop('files')[0];

//    if (file == undefined)
//         return "";

//     const nombre = 'images/'+file.name;
//     const storageRef = ref(storage, nombre);



//     await uploadBytesResumable(storageRef, file);
//     return await getDownloadURL(storageRef);
//     }

// return await

//       const uploadImage = async () => {
//   const filename = new Date().getTime() + photo!.name
//   const storage = getStorage(app)
//   const storageRef = ref(storage, filename)
//   await uploadBytesResumable(storageRef, photo!);
//   return await getDownloadURL(storageRef);
// }


function mostrarDatos(informacion, actionUrl) {





    let saludo = ("Hola " + $("#nombre_derecho").val() + ", verifica que los datos que ingresaste sean correctos:");
    let contenido =
        "<br><br>DATOS GENERALES" +
        "<br>CENDI: " + informacion.cendi +
        "<br>Folio: " + informacion.folio +
        "<br>Grupo: " + informacion.grupo +

        "<br><br>INFORMACIÓN DEL NIÑO O LA NIÑA" +
        "<br>Nombre: " + informacion.nombre +
        "<br>Primer Apellido: " + informacion.primer_apellido +
        "<br>Segundo Apellido: " + informacion.segundo_apellido +
        "<br>Fecha de nacimiento: " + informacion.fecha_nacimiento +
        "<br>Edad: " + informacion.edadAnios + "años, " + informacion.edadMeses + "meses " +
        "<br>Email: " + informacion.email +
        "<br>CURP: " + informacion.curp +

        "<br><br>INFORMACIÓN DEL O LA DERECHOHABIENTE" +
        "<br>Nombre: " + informacion.nombre_derecho +
        "<br>Primer Apellido: " + informacion.primer_apellido_derecho +
        "<br>Segundo Apellido: " + informacion.segundo_apellido_derecho +
        "<br>Calle: " + informacion.calle +
        "<br>No. Externo: " + informacion.noExt +
        "<br>No. Int: " + informacion.noInt +
        "<br>Colonia: " + informacion.colonia +
        "<br>Alcaldia: " + informacion.alcaldia +
        "<br>Entidad: " + informacion.entidad +
        "<br>Codigo Postal: " + informacion.cp +
        "<br>Telefono Fijo: " + informacion.telefono_fijo +
        "<br>Telefono Celular: " + informacion.telefono_celular +
        "<br>Email Derecho: " + informacion.email_derecho +
        "<br>Ocupacion: " + informacion.ocupacion +
        "<br>Curp" + informacion.curp_derecho +
        "<br>Puesto: " + informacion.puesto +
        "<br>Sueldo: " + informacion.sueldo +
        "<br>Numero de Empleado: " + informacion.numero_empleado +
        "<br>Adscripcion: " + informacion.adscripcion +
        "<br>Horario: " + informacion.horario +
        "<br>Extension: " + informacion.extension +

        "<br><br>INFORMACIÓN DEL O DE LA CONYUGE" +
        "<br>Tiene conyuge: " + informacion.tienec +
        "<br>Primer Apellido: " + informacion.primer_apellido_conyuge +
        "<br>Segundo Apellido: " + informacion.segundo_apellido_conyuge +
        "<br>Nombre: " + informacion.nombre_conyuge +
        "<br>Calle: " + informacion.calle_conyuge +
        "<br>No. Ext: " + informacion.noExt_conyuge +
        "<br>No. Int: " + informacion.noInt_conyuge +
        "<br>Colonia: " + informacion.colonia_conyuge +
        "<br>Alcaldia: " + informacion.alcaldia_conyuge +
        "<br>Entidad: " + informacion.entidad_conyuge +
        "<br>Codigo Postal: " + informacion.cp_conyuge +
        "<br>Telefono Fijo: " + informacion.telefono_fijo_conyuge +
        "<br>Telefono Celular: " + informacion.telefono_celular_conyuge +
        "<br>Lugar de Trabajo: " + informacion.lugar_trabajo_conyuge +
        "<br>Domicilio de Trabajo: " + informacion.domicilio_trabajo_conyuge +
        "<br>Telefono de Trabajo: " + informacion.telefono_trabajo_conyuge +
        "<br>Extension: " + informacion.extension_conyuge;



    return Swal.fire({
        title: saludo,
        html: contenido,
        // text: contenido,
        // imageUrl: "https://www.ipn.mx/assets/files/saes/img/escudosNS/IPN-Default.png",
        // imageWidth: 400,
        // imageHeight: 200,
        // imageAlt: 'Custom image',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Aceptar',
        cancelButtonText: 'Modificar'
    }).then((result) => {
        if (result.isConfirmed) {

            enviaJSON(informacion, actionUrl);


        }
    }).error(function () {
        return false;
    }).error(function () {
        return false;
    });
}


$("#formulario").submit(function (e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var actionUrl = form.attr('action');

    let fotoURL = "https://www.ipn.mx/assets/files/saes/img/escudosNS/IPN-Default.png";

    // subeFoto( informacion, actionUrl);
    var informacion = {

        cendi: $('#cendi').val(),
        foto: "../assets/man.jpg",
        folio: $('#folio').val(),
        grupo: $('#grupo').val(),

        //Datos niño
        primer_apellido: $('#primer_apellido').val(),
        segundo_apellido: $('#segundo_apellido').val(),
        nombre: $('#nombre').val(),
        fecha: $('#fecha').val(),
        edadAnios: $('#edadAnios').val(),
        edadMeses: $('#edadMeses').val(),
        email: $('#email').val(),
        curp: $('#curp').val(),

        //Datos de derechohabiente
        foto_derecho: "../assets/man.jpg",
        primer_apellido_derecho: $('#primer_apellido_derecho').val(),
        segundo_apellido_derecho: $('#segundo_apellido_derecho').val(),
        nombre_derecho: $('#nombre_derecho').val(),
        calle: $('#calle').val(),
        noExt: $('#noExt').val(),
        noInt: $('#noInt').val(),
        colonia: $('#colonia').val(),
        alcaldia: $('#alcaldia').val(),
        entidad: $('#entidad').val(),
        cp: $('#cp').val(),
        telefono_fijo: $('#telefono_fijo').val(),
        telefono_celular: $('#telefono_celular').val(),
        email_derecho: $('#email_derecho').val(),
        ocupacion: $('#ocupacion').val(),
        curp_derecho: $('#curp_derecho').val(),
        puesto: $('#puesto').val(),
        sueldo: $('#sueldo').val(),
        numero_empleado: $('#numero_empleado').val(),
        adscripcion: $('#adscripcion').val(),
        horario: $('#horario').val(),
        extension: $('#extension').val(),
        foto_autorizada: "../assets/man.jpg",
        //Datos del conyuge
        foto_conyuge: "../assets/man.jpg",
        tienec: $('#tienec').val(),
        primer_apellido_conyuge: $('#primer_apellido_conyuge').val(),
        segundo_apellido_conyuge: $('#segundo_apellido_conyuge').val(),
        nombre_conyuge: $('#nombre_conyuge').val(),
        calle_conyuge: $('#calle_conyuge').val(),
        noExt_conyuge: $('#noExt_conyuge').val(),
        noInt_conyuge: $('#noInt_conyuge').val(),
        colonia_conyuge: $('#colonia_conyuge').val(),
        alcaldia_conyuge: $('#alcaldia_conyuge').val(),
        entidad_conyuge: $('#entidad_conyuge').val(),
        cp_conyuge: $('#cp_conyuge').val(),
        telefono_fijo_conyuge: $('#telefono_fijo_conyuge').val(),
        telefono_celular_conyuge: $('#telefono_celular_conyuge').val(),
        lugar_trabajo_conyuge: $('#lugar_trabajo_conyuge').val(),
        domicilio_trabajo_conyuge: $('#domicilio_trabajo_conyuge').val(),
        telefono_trabajo_conyuge: $('#telefono_trabajo_conyuge').val(),
        extension_conyuge: $('#extension_conyuge').val()

    };


    alumno = informacion;

    //        mostrarDatos(informacion, actionUrl);

});

$('#btn-imprimir').hide();
$('#btn-imprimir').click(function () {
    let direc = "../back/pdf/generatePDF.php?folio=" + alumno.folio;
    window.open(direc, '_blank');
});


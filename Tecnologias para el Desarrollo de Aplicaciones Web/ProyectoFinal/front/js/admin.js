$(document).ready(function () {
    $("#navegacion").load("./compartidos/barranavadmin.html");
    $("#futer").load("./compartidos/futer.html");
    $("#contenido1").load("./compartidos/formol.html");
    jalaTodo();

    //Activaciones
   // $('select').formSelect(); //jala select
    $('input#input_text, textarea#textarea2').characterCounter(); // jala counter

    var alumnos;
    var contenedor = $('#alumnos');

    //Carga cada uno de los registros de los alumnos a la página
    function construye() {
        let nuevaLista = "<div class='accordion' id='alumnos'> ";
        for (let index = 0; index < alumnos.length; index++) {
           // "<p>hola</p>";
            let nuevoAlumno = "";
            nuevoAlumno += ("<div class='accordion-item' id='usr"+index+"' >");
           // nuevoAlumno += ("    <img src='" + alumnos[index].Imagen_Ninio + "' alt='" + alumnos[index].Folio + "' class='rounded float-start' >");
            nuevoAlumno += ("   <div class='accordion-header' id='encabezado"+index+"'>");
            
         //   nuevoAlumno += ("       <button class='accordion-button collapsed ver-mas' type='button' data-bs-toggle='collapse' data-bs-target='#alumno"+index+"' aria-expanded='false' aria-controls='collapse"+index+"'>"+ alumnos[index].Folio +"</button>");
            nuevoAlumno += ("       <div  class='accordion-button collapsed ver-mas btn d-flex' data-bs-toggle='collapse' data-bs-target='#alumno"+index+"' aria-expanded='false' aria-controls='collapse"+index+"'>");
            nuevoAlumno += ("           <img src='./assets/man.jpg' class='rounded-circle img-responsive float-left mx-3' width='50' height='50' alt='100x100' data-holder-rendered='true'></img>");
            nuevoAlumno += ("           <p>"+ alumnos[index].Folio +"</p>");
            nuevoAlumno += ("           <br>");
            //nuevoAlumno += ("         <p>"+ alumnos[index].Curp +"</p>");
          //  nuevoAlumno += ("           <button class='btn btn-primary ver-mas float-end'>Ver más</button>");
            nuevoAlumno += ("       </div>");
            nuevoAlumno += ("   </div>")
            
            nuevoAlumno += ("   <div id='alumno"+index+"' class='accordion-collapse collapse' aria-labelledby='encabezado"+index+"' data-bs-parent='#alumnos' >");
            nuevoAlumno += ("            <div class='accordion-body'>");
            // nuevoAlumno += ("        <a class='col btn ver-mas'>Ver mas</a>");
            // nuevoAlumno += ("        <a class='col btn ver-menos'>Ver menos</a>");
            nuevoAlumno += ("       <div class='buttons float-end'>");
            nuevoAlumno += ("        <a class='col btn editar'>Editar</a>");
            nuevoAlumno += ("        <a class='col btn cancelar-edicion'>Cancelar edicion</a>");
            nuevoAlumno += ("        <a class='col btn btn-reset'>Restablecer valores</a>");
            nuevoAlumno += ("        <a class='col right btn btn-danger elimina'>Eliminar</a>");
            nuevoAlumno += ("       </div>");
            nuevoAlumno += ("       <form id='formula"+index+"' class='formula' action='../back/BD/ActualizarDatos.php' method='get'>");
            nuevoAlumno += ("       </form>");
            nuevoAlumno += ("           </div>");
            nuevoAlumno += ("    </div>");
            nuevoAlumno += ("</div>");
            nuevaLista += nuevoAlumno;
        }
        nuevaLista += "</div>";
        contenedor.replaceWith(nuevaLista);
        contenedor = $('#alumnos');

    }
    ///Generar a partir de la query al back

    ///Nested functions para controlar el dom
    function restableceValores(alumnRow, idx) {
        alumnRow.find('#cendi').val(alumnos[idx].Cendi);
        //alumnRow.find('.foto').val(alumnos[idx].foto);
        alumnRow.find('#folio').val(alumnos[idx].Folio);
        alumnRow.find('#grupo').val(alumnos[idx].Grupo);

        //Datos niño
        alumnRow.find('#primer_apellido').val(alumnos[idx].Primer_Apellido);
        alumnRow.find('#segundo_apellido').val(alumnos[idx].Segundo_Apellido);
        alumnRow.find('#nombre').val(alumnos[idx].Nombre);
        alumnRow.find('#fecha').val(alumnos[idx].FechaNac);
        alumnRow.find('#edadAnios').val(alumnos[idx].Edad_Anios);
        alumnRow.find('#edadMeses').val(alumnos[idx].Edad_Meses);
        alumnRow.find('#email').val(alumnos[idx].Email);
        alumnRow.find('#curp').val(alumnos[idx].Curp);

        //Datos de derechohabiente
        alumnRow.find('#primer_apellido_derecho').val(alumnos[idx].Primer_Apellido_Derecho);
        alumnRow.find('#segundo_apellido_derecho').val(alumnos[idx].Segundo_Apellido_Derecho);
        alumnRow.find('#nombre_derecho').val(alumnos[idx].Nombre_Derecho);
        alumnRow.find('#calle').val(alumnos[idx].calle);
        alumnRow.find('#noExt').val(alumnos[idx].noExt);
        alumnRow.find('#noInt').val(alumnos[idx].noInt);
        alumnRow.find('#colonia').val(alumnos[idx].colonia);
        alumnRow.find('#alcaldia').val(alumnos[idx].alcaldia);
        alumnRow.find('#entidad').val(alumnos[idx].entidad);
        alumnRow.find('#cp').val(alumnos[idx].cp);
        alumnRow.find('#telefono_fijo').val(alumnos[idx].Telefono_Fijo_Derecho);
        alumnRow.find('#telefono_celular').val(alumnos[idx].Telefono_Celular_Derecho);
        alumnRow.find('#email_derecho').val(alumnos[idx].Email_Derecho);
        alumnRow.find('#ocupacion').val(alumnos[idx].Ocupacion_Derecho);
        alumnRow.find('#curp_derecho').val(alumnos[idx].Curp_Derecho);
        alumnRow.find('#puesto').val(alumnos[idx].Puesto);
        alumnRow.find('#sueldo').val(alumnos[idx].Sueldo);
        alumnRow.find('#numero_empleado').val(alumnos[idx].Numero_Empleado);
        alumnRow.find('#adscripcion').val(alumnos[idx].Adscripcion);
        alumnRow.find('#horario').val(alumnos[idx].Horario_Trabajo);
        alumnRow.find('#extension').val(alumnos[idx].Extension);

        //Datos del conyuge
        alumnRow.find('#tienec').val(alumnos[idx].tienec);
        alumnRow.find('#primer_apellido_conyuge').val(alumnos[idx].Primer_Apellido_Conyuge);
        alumnRow.find('#segundo_apellido_conyuge').val(alumnos[idx].Segundo_Apellido_Conyuge);
        alumnRow.find('#nombre_conyuge').val(alumnos[idx].Nombre_Conyuge);
        alumnRow.find('#calle_conyuge').val(alumnos[idx].calle_conyuge);
        alumnRow.find('#noExt_conyuge').val(alumnos[idx].noExt_conyuge);
        alumnRow.find('#noInt_conyuge').val(alumnos[idx].noInt_conyuge);
        alumnRow.find('#colonia_conyuge').val(alumnos[idx].colonia_conyuge);
        alumnRow.find('#alcaldia_conyuge').val(alumnos[idx].alcaldia_conyuge);
        alumnRow.find('#entidad_conyuge').val(alumnos[idx].entidad_conyuge);
        alumnRow.find('#cp_conyuge').val(alumnos[idx].cp_conyuge);
        alumnRow.find('#telefono_fijo_conyuge').val(alumnos[idx].Telefono_Fijo_Conyuge);
        alumnRow.find('#telefono_celular_conyuge').val(alumnos[idx].Telefono_Celular_Conyuge);
        alumnRow.find('#lugar_trabajo_conyuge').val(alumnos[idx].Lugar_Trabajo_Conyuge);
        alumnRow.find('#domicilio_trabajo_conyuge').val(alumnos[idx].Domicilio_Trabajo_Conyuge);
        alumnRow.find('#telefono_trabajo_conyuge').val(alumnos[idx].Telefono_Trabajo_Conyuge);
        alumnRow.find('#extension_conyuge').val(alumnos[idx].Extension);
        M.updateTextFields();

    }

    //Habilita los campos
    function activarForm(alumnRow, formID) {
        alumnRow.find(formID).find(':input:disabled').prop('disabled', false);
        alumnRow.find('.btn-enviar').show();
    }

    //Deshabilita los campos
    function bloquearForm(alumnRow, formID) {
        alumnRow.find(formID).find(':input:not(:disabled)').prop('disabled', true);
        alumnRow.find('.btn-enviar').hide();
    }

    //Muestra los botones y habilita los campos
    function activarEdicion(alumnRow, formID) {
        alumnRow.find(".editar").hide();
        alumnRow.find(".cancelar-edicion").show();
        alumnRow.find(".btn-reset").show();
        activarForm(alumnRow, formID);
    }

    //Ocultalos botones y deshabilita los campos
    function cancelarEdicion(alumnRow, formID) {
        alumnRow.find(".editar").show();
        alumnRow.find(".cancelar-edicion").hide();
        alumnRow.find(".btn-reset").hide();
        bloquearForm(alumnRow, formID);
    }


    function verMas(alumnRow, formID) {
        alumnRow.find(formID).show();
        alumnRow.find(".ver-menos").show();
      //  alumnRow.find(".ver-mas").hide();
        cancelarEdicion(alumnRow, formID);
    }

    function verMenos(alumnRow, formID) {
        alumnRow.find(formID).hide();
        alumnRow.find(".ver-mas").show();
        alumnRow.find(".ver-menos").hide();
        alumnRow.find(".editar").hide();
        alumnRow.find(".cancelar-edicion").hide();
        alumnRow.find(".btn-reset").hide();
        bloquearForm(alumnRow, formID);
    }

    function cargaControllers() {
        for (let index = 0; index < alumnos.length; index++) {
            const element = alumnos[index];
            let formID = ("#formula" + index);
            let alumnID = ("#usr"+index);
            $(formID).load("./compartidos/formRegistro.html").ready(function () {
               // $('select').formSelect();
                
                M.updateTextFields();
                let form = $(this);
                ///Enviar un formulario a actualizar
                /*$(formID).submit(function (e) {
                    //alert("Voy a subir");
                    e.preventDefault(); // avoid to execute the actual submit of the form.
                    let subitForm = $(this);
                    let actionUrl = subitForm.attr('action');
                    let alumno = $(formID).serialize();
                    alert("Tengo para subir el yeison" + alumno);
                    $.ajax({
                        type: "GET",
                        url: actionUrl,
                        //data: form.serialize(), // serializes the form's elements.
                        data: alumno,
                        success: function (data) {
                            //alert("respondido");
                            // show response from the php script.
                            let jsonData = $.parseJSON(data);
                            console.log(data);
                            //subitForm.find('.correo').val("Enviado chido" + jsonData.curpo);
                        }
                    });
                });*/
               // $('select').formSelect();
            });
            //$(alumnID).ready(function() {
            M.updateTextFields();
            let alumInicial = $(alumnID);
            verMenos(alumInicial, formID);
            restableceValores(alumInicial, index);

            $(alumnID).find(".ver-mas").click(function () {
                let alumRow = $(alumnID);
                $("#hola").hide();
                verMas(alumRow, formID);
                restableceValores(alumInicial, index);
            });
            $(alumnID).find(".ver-menos").not(".collapsed").click(function () {
                let alumRow = $(alumnID);
                $("#hola").show();
                verMenos(alumRow, formID);
                restableceValores(alumRow, index);
            });
            $(alumnID).find(".editar").click(function () {
                let alumRow = $(alumnID);
                activarEdicion(alumRow, formID);
               // $('select').formSelect();
            });
            $(alumnID).find(".cancelar-edicion").click(function () {
                let alumRow = $(alumnID);
                cancelarEdicion(alumRow, formID);
                restableceValores(alumRow, index);
            });
            $(alumnID).find(".btn-reset").click(function () {
                let alumRow = $(alumnID);

                restableceValores(alumRow, index);
                //$(this).closest(alumnID).find('.contrasena').val(alumnos[index].nombre);

            });
            
            $(alumnID).find('.elimina').click(function () {
                $(('#usr' + index)).replaceWith("");
                $.ajax({
                    type: "GET",
                    url: '../back/BD/EliminarDatos.php?folioBorrar=' + alumnos[index].Folio,
                    success: function (response) {
                        let jsonData = JSON.parse(response);
                        $(alumnID).replaceWith("");
                        // user is logged in successfully in the back-end
                        // let's redirect
                        if (jsonData.state == "0") {
                            //location.href = 'inicio.html';
                            alert(jsonData.arre[0]);
                        } else {
                            alert('Invalid Credentials!');
                        }
                    }
                });
            });

        }
    }

    function jalaTodo() {
        let direc = "../back/BD/DatosBD.php";
        $.ajax({
            type: "GET",
            url: direc,
            success: function (data) {

                let jsonData = $.parseJSON(data);
                alumnos = jsonData;
                construye();
                cargaControllers();
            }
        });
    }

    $('#actualizar').click(function () {
        jalaTodo();
    });

    $('#hola').click(function(){
        $('#hola').hide();

    }

    )
});
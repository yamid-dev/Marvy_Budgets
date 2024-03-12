
//Funcion para enviar formularios
function enviar(formulario,boton){
    const form = document.getElementById(`${formulario}`);
    const botonEnviar = document.getElementById(`${boton}`);

    botonEnviar.addEventListener('click',()=>{
        form.submit();
    });
}

//funcion para mostrar mensajes
function mostrarMensaje() {
    var mensaje = document.getElementById('mensaje');
    var contenidoMensaje = document.getElementById('contenidoMensaje');
    var valor = contenidoMensaje.dataset.value;

    if (contenidoMensaje.innerHTML.trim() !== ''){
        mensaje.style.display = 'flex'; // Mostrar el mensaje si hay contenido
        setTimeout(function() {
            mensaje.style.display = 'none'; // Ocultar el mensaje después de 3 segundos
        }, 3000);
        if (valor=='True'){
            window.location.href="/home"
        };
    } else {
        mensaje.style.display = 'none'; // Ocultar el mensaje si no hay contenido
    }
}

// Llamar a la función para mostrar el mensaje cuando se cargue la página
window.onload = function() {
    mostrarMensaje();
};


//funciones de cerrar y abrir menu

function cerrar(){
    const menu = document.getElementById('menu-desplegable');
    const home = document.getElementById('home');
    menu.style.display="none";
    home.style.gridTemplateColumns="1fr 1fr 1fr";
    home.style.gridTemplateRows="10% 1fr";
};

function abrir(){
    const menu= document.getElementById('menu-desplegable');
    const home = document.getElementById('home');

    home.style.gridTemplateColumns="1fr 1fr 1fr 1fr";
    home.style.gridTemplateRows="10% 1fr";
    menu.style.display="block";
}

//Funcion para cerrar sesión
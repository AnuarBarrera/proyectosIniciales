// Variables
const titulo = "Desarrollador Web y Móvil";
const parrafoIntroductorio = "Bienvenido a mi CV en línea. Soy Anuar Barrera Yeeben, un desarrollador apasionado por crear soluciones tecnológicas innovadoras.";
const historialLaboral = [
  { empresa: "Citi Mexico", cargo: "Client Onboarding Analyst", fecha: "2023-a la fecha" },
  { empresa: "Banco Nacional de México", cargo: "Asesor Telefónico", fecha: "2016-2023" },
];
const proyectos = [
  { nombre: "Proyecto X", descripcion: "Desarrollo de una aplicación web para gestión de proyectos", tecnologias: ["HTML", "CSS", "JavaScript"] },
  { nombre: "Proyecto Y", descripcion: "Desarrollo de una aplicación móvil para entrega de comida", tecnologias: ["Java", "Android"] },
];
const redesSociales = [
  { nombre: "GitHub", url: "https://www.github.com/AnuarBarrera" },
  { nombre: "LinkedIn", url: "https://www.linkedin.com/in/AnuarBarrera" },
];
const fotos = [
  { url: "foto1.jpg", descripcion: "Foto 1" },
  { url: "foto2.jpg", descripcion: "Foto 2" },
  { url: "foto3.jpg", descripcion: "Foto 3" },
];

// Funciones
function crearTitulo() {
  const tituloElement = document.querySelector(".Title");
  tituloElement.textContent = titulo;
}

function crearParrafoIntroductorio() {
  const parrafoElement = document.querySelector(".Parrafo-entrada");
  parrafoElement.textContent = parrafoIntroductorio;
}

function crearBotonesAcceso() {
  const linksAccesosElement = document.querySelector(".Links-accesos");
  const botones = [
    { texto: "Historial Laboral", url: "#historial-laboral" },
    { texto: "Proyectos", url: "#proyectos" },
    { texto: "Redes Sociales", url: "#redes-sociales" },
  ];
  botones.forEach((boton) => {
    const botonElement = document.createElement("button");
    botonElement.textContent = boton.texto;
    botonElement.onclick = () => {
      const seccion = document.querySelector(boton.url);
      seccion.scrollIntoView({ behavior: "smooth" });
    };
    linksAccesosElement.appendChild(botonElement);
  });
}

function crearCarruselFotos() {
  const fotosElement = document.querySelector(".fotos");
  const carruselElement = document.createElement("div");
  carruselElement.classList.add("carrusel");
  fotos.forEach((foto) => {
    const fotoElement = document.createElement("img");
    fotoElement.src = foto.url;
    fotoElement.alt = foto.descripcion;
    carruselElement.appendChild(fotoElement);
  });
  fotosElement.appendChild(carruselElement);
}

function crearHistorialLaboral() {
  const historialLaboralElement = document.createElement("div");
  //(link unavailable) = "historial-laboral";
  historialLaboral.forEach((experiencia) => {
    const experienciaElement = document.createElement("p");
    experienciaElement.textContent = `${experiencia.empresa} - ${experiencia.cargo} (${experiencia.fecha})`;
    historialLaboralElement.appendChild(experienciaElement);
  });
  document.body.appendChild(historialLaboralElement);
}

function crearProyectos() {
  const proyectosElement = document.createElement("div");
  //(link unavailable) = "proyectos";
  proyectos.forEach((proyecto) => {
    const proyectoElement = document.createElement("p");
    proyectoElement.textContent = `${proyecto.nombre} - ${proyecto.descripcion} (${proyecto.tecnologias.join(", ")})`;
    proyectosElement.appendChild(proyectoElement);
  });
  document.body.appendChild(proyectosElement);
}

function crearRedesSociales() {
  const redesSocialesElement = document.createElement("div");
  //(link unavailable) = "redes-sociales";
  redesSociales.forEach((red) => {
    const redElement = document.createElement("p");
    redElement.textContent = `${red.nombre} - ${red.url}`;
    redesSocialesElement.appendChild(redElement);
  });
  document.body.appendChild(redesSocialesElement);
}

// Inicialización
document.addEventListener("DOMContentLoaded", function() {
  crearTitulo();
  crearParrafoIntroductorio();
  crearBotonesAcceso();
  crearCarruselFotos();
  crearHistorialLaboral();
  crearProyectos();
  crearRedesSociales();
});

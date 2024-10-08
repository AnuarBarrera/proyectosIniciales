// Función para agregar título y párrafo
document.addEventListener('DOMContentLoaded', function () {
  // Título
  document.querySelector('.Title').innerText = "Curriculum Vitae en Línea - Anuar Barrera";

  // Párrafo introductorio
  document.querySelector('.Parrafo-entrada').innerText = "Bienvenido a mi CV en línea. Aquí encontrarás información sobre mi trayectoria profesional, proyectos destacados y enlaces a mis redes sociales. Explora y conoce más sobre mi trabajo como desarrollador.";

  // Crear botones de acceso
  let linksAccesos = document.querySelector('.Links-accesos');

  let historialButton = document.createElement('button');
  historialButton.innerText = "Historial Laboral";
  historialButton.onclick = function () {
    alert('Historial Laboral - Esta sección está en construcción.');
  };

  let proyectosButton = document.createElement('button');
  proyectosButton.innerText = "Proyectos";
  proyectosButton.onclick = function () {
    alert('Proyectos - Esta sección está en construcción.');
  };

  let githubButton = document.createElement('a');
  githubButton.innerText = "GitHub";
  githubButton.href = "https://github.com/tuusuario";  // Reemplaza por tu enlace de GitHub
  githubButton.target = "_blank";

  let linkedinButton = document.createElement('a');
  linkedinButton.innerText = "LinkedIn";
  linkedinButton.href = "https://www.linkedin.com/in/tuusuario";  // Reemplaza por tu enlace de LinkedIn
  linkedinButton.target = "_blank";

  // Añadir botones al contenedor
  linksAccesos.appendChild(historialButton);
  linksAccesos.appendChild(proyectosButton);
  linksAccesos.appendChild(githubButton);
  linksAccesos.appendChild(linkedinButton);

  // Carrusel de fotos
  const fotos = ["foto1.jpg", "foto2.jpg", "foto3.jpg"]; // Añade aquí las rutas de tus fotos
  let currentFotoIndex = 0;
  let fotosContainer = document.querySelector('.fotos');

  let imgElement = document.createElement('img');
  imgElement.src = fotos[currentFotoIndex];
  fotosContainer.appendChild(imgElement);

  setInterval(() => {
    currentFotoIndex = (currentFotoIndex + 1) % fotos.length;
    imgElement.src = fotos[currentFotoIndex];
  }, 3000); // Cambia de foto cada 3 segundos
});

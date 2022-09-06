let nombre = 'Guido';
let apellido = 'Pruzzo';

let estudiante = `${nombre} ${apellido}`;
console.log(estudiante);

let estudianteMayus = estudiante.toUpperCase();
console.log(estudianteMayus);

let estudianteMinus = estudianteMayus.toLowerCase();
console.log(estudianteMinus);

let contadorCadena = estudiante.length;
console.log(contadorCadena);

let primeraLetraNombre = nombre[0];
console.log(primeraLetraNombre);

let primeraLetraApellido = apellido[0];
console.log(primeraLetraApellido);

let estudianteSinEspacios = estudiante.replace(/ /g, "");
console.log(estudianteSinEspacios);

let encontrarNombre = estudiante.includes(nombre);
console.log(encontrarNombre);
let hoy = new Date();
console.log(hoy);

let miNacimiento = new Date(1997, 05, 19);
console.log(miNacimiento);

console.log(hoy > miNacimiento);

let miMes = miNacimiento.getMonth() + 1;
console.log(miMes);

let miAnio = miNacimiento.getFullYear();
console.log(miAnio);
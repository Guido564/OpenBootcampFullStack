let listaCompra = ['Arroz', 'Huevos', 'Salsa de tomates', 'Manzanas', 'Tomates']
listaCompra.push('Aceite de Girasol')
console.log(listaCompra)
listaCompra.pop('Aceite de Girasol')
console.log(listaCompra)

let peliculasFavoritas = [{titulo: 'La haine', director: 'Mathieu Kassovitz', fecha: 1995}, {titulo: 'Texas Chain Saw Massacre', director: 'Tobe Hooper', fecha: 1974}, {titulo: 'The lighthouse', director: 'Robert Eggers', fecha: 2019}]
console.log(peliculasFavoritas)

const filtrarFecha = peliculasFavoritas.filter(obj => obj.fecha < 2010)
console.log(filtrarFecha)

const directores = peliculasFavoritas.map((obj) => obj.director)
console.log(directores)

const titulos = peliculasFavoritas.map((obj) => obj.titulo)
console.log(titulos)

const directorTitulo = [...directores, ...titulos]
console.log(...directorTitulo)

console.log(directores.concat(titulos))
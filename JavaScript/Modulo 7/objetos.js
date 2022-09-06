let misDatos = {
    nombre: 'Guido',
    apellido: 'Pruzzo',
    edad: 25,
    altura: 182,
    soyDesarrollador: true,
}

let miEdad = misDatos.edad
console.log(miEdad)

let mejoresAmigos = {
    pichu: {
        nombre: 'Agustin',
        apellido: 'Vergara',
        edad: 25,
        altura: 175,
        esDesarrollador: true,
    },

    lonchi: {
        nombre: 'Leonel',
        apellido: 'Daglio',
        edad: 25,
        altura: 170,
        esDesarrollador: true,
    }
}
console.log(mejoresAmigos)

let misDatosLista = [{ ...misDatos }]
console.log(misDatosLista)
let lista2 = misDatosLista.concat(mejoresAmigos.lonchi, mejoresAmigos.pichu)
console.log(lista2)

lista2.sort((a, b) => a.altura - b.altura)
console.log(lista2)
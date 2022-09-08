class Estudiante {
    constructor(nombre, asignaturas) {
        this.nombre = nombre
        this.asignaturas = asignaturas
    }

    obtenDatos() {
        console.log(`Hola buenos dias senioras y seniores mi nombre es ${this.nombre}, soy aspirante de programador y actualmente estoy viendo: ${this.asignaturas}`)
    }
}

const estudiante_ejemplar = new Estudiante('Guido', ['CSS', ' HTML', ' JavasCript'])
console.log(estudiante_ejemplar.obtenDatos())
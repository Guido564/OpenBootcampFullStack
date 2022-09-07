function devuelvoUnaGilada() {
    return true
}

console.log(devuelvoUnaGilada())

function holaEn5Segundos() {
    console.log('Hola pasaron 5 segundos');
}

setTimeout(holaEn5Segundos, 5000);

function* generaId() {
    let id = 0
    while (true) {
        id++
        if (id % 2 == 0) {
            yield id
        }
    }
}

const gen = generaId();

console.log(gen.next())
console.log(gen.next())
console.log(gen.next())
console.log(gen.next())
console.log(gen.next())
console.log(gen.next())
console.log(gen.next())
console.log(gen.next())


const logger = require("./logger");


const miFuncion = nombre => {
  if (typeof nombre === 'string' && nombre.length > 4) {
    return `Hola ${nombre}, como le va en este bello dia?`
  }
  throw new Error('Por favor ingrese un nombre valido')
}

const nom = 'Guido';

try {
  logger.info('Funcion ejecutandose de manera conforme')
  const saludo = miFuncion(nom)
  console.log(saludo)
} catch (e) {
  logger.error(`Nanana te mandaste cualquiera: ${e}`)
  logger.error('ERROR ERROR')
} finally {
  logger.info('Programa finalizado')
}
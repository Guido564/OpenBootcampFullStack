from pip import main
import pprint
import operaciones.operaciones as op

def main():
    suma = op.suma(2,2)
    resta = op.resta(10,5)
    multiplicacion = op.multiplicacion(7,100)
    division = op.division(21,3)
    pprint.pprint((suma, resta, multiplicacion, division))


if __name__ == "__main__":
    main()
class Alumno:
    nombre = None
    nota = None

    def aprobado(self):
        if(self.nota >= 6):
            return "El alumno " + self.nombre + " se encuentra aprobado con un: " + str(self.nota)
        else:
            return "El alumno " + self.nombre + " se encuentra desaprobado con un: " + str(self.nota)

a = Alumno()
a.nombre = "Juan"
a.nota = 4
print(a.aprobado())
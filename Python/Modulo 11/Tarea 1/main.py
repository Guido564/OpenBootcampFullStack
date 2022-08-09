from distutils.log import info
from multiprocessing import connection
import sqlite3

def main():
    pass

conn = sqlite3.connect('tarea.db')
cursor = conn.cursor()
print("La conexion con sqlite3 se ha establecido satisfactoriamente")

def agregarAlumno(id, nombre, apellido):
    try:
        conn = sqlite3.connect('tarea.db')
        cursor = conn.cursor()
        print("Se ha inicializado la funcion para agregar usuario a la base de datos")
        
        insertar = """INSERT INTO alumnos(id, nombre, apellido) VALUES (?, ?, ?)"""
        dataTupla = (id, nombre, apellido)
        cursor.execute(insertar, dataTupla)
        conn.commit()
        print("Se ha agregado correctamente el usuario")
        
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")

def buscarAlumno(id):
    try:
        conn = sqlite3.connect('tarea.db')
        cursor = conn.cursor()
        print("Se ha inicializado correctamenta la busqueda de usuarios")
        
        seleccion = """select * from alumnos where id = ?"""
        cursor.execute(seleccion, (id))
        info = cursor.fetchall()
        print("ID del alumno: " + id)
        for row in info:
            print("Nombre: ", row[1])
            print("Apellido: ", row[2])
        cursor.close()
    
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")

    
rows = cursor.execute('SELECT * FROM alumnos')
for row in rows:
    print(row)
    
cursor.close()
conn.close()


agregarAlumno(0, "Franz", "Kafka")
buscarAlumno("0")


if __name__ == "__main__":
    main()
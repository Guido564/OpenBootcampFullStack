public class Main {
    public static void main(String[] args) {
            Cliente cliente = new Cliente();
            cliente.nombre = "Osvaldo Sebastian";
            cliente.edad = 33;
            cliente.telefono = 342537;
            cliente.credito = "Credito Argentino";
            System.out.println("Los datos del cliente son -Nombre: " + cliente.nombre + " -Edad: " + cliente.edad + " -Telefono: " + cliente.telefono + " -Credito: " + cliente.credito);


            Trabajador trabajador = new Trabajador();
            trabajador.nombre = "Marco Antonio";
            trabajador.edad = 27;
            trabajador.telefono = 342381;
            trabajador.salario = 45000;
            System.out.println("Los datos del trabajador son -Nombre: " + trabajador.nombre + " -Edad: " + trabajador.edad + " -Telefono: " + trabajador.telefono + " -Salario: " + trabajador.salario);
    }
}

class Persona {
    String nombre;
    int edad;
    int telefono;
}

class Cliente extends Persona {
    String credito;
}

class Trabajador extends Persona {
    int salario;
}
public class Main {
    public static void main(String[] args) {
        int numerolf = 110;

        if(numerolf > 0) {
            System.out.println("El numero ingresado es positivo");
        } else if(numerolf < 0) {
            System.out.println("El numero ingrsado es negativo");
        } else {
            System.out.println("El numero ingresado es 0");
        }

        int numeroWhile = 0;

        while (numeroWhile < 3){
            System.out.println(numeroWhile);
            numeroWhile++;
        }

        do{
            System.out.println(numeroWhile);
            numeroWhile++;
        } while (numeroWhile < 3);

        int numeroFor = 0;

        for(; numeroFor <= 3; numeroFor++){
            System.out.println(numeroFor);
        }

        var estacion = "Bad Bunny";

        switch (estacion){
            case "Verano":
                System.out.println("Hora de ir a la playa");
                break;
            case "Invierno":
                System.out.println("A abrigarse");
                break;
            case "Primavera":
                System.out.println("Hora de empezar la huerta");
                break;
            case "Otonio":
                System.out.println("A limpiar las hojas de la vereda");
                break;
            default:
                System.out.println("EL valor ingresado no corresponde a una estacion del anio");

        }

    }

}
public class Main {
    public static void main(String[] args) {
        auto miAuto = new auto();
        miAuto.AgregarPuerta();
        miAuto.AgregarPuerta();
        System.out.println(miAuto.puertas);
    }
}

class auto {
    public int puertas = 2;

    public void AgregarPuerta(){
        this.puertas++;
    }
}
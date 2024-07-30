package tad;
import java.util.ArrayList;
public class TAD {
    public static void main(String[] args) {
        ArrayList <DatosLineales> Datos = new ArrayList();
        Datos.add(new Lista());
        Datos.add(new Pila());
        Datos.add(new Cola());
        for(DatosLineales D:Datos)
            D.agregarDato("Hola");
        for(DatosLineales D:Datos)
            D.obtenerDato();
    }
}

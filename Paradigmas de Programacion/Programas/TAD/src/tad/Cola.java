package tad;
import java.util.LinkedList;
public class Cola extends DatosLineales{
     LinkedList cola=new LinkedList();
    public void agregarDato(String n){
        this.cola.add(n);
        System.out.println("Se guardo el dato en la Cola");
    }
    @Override
    public void obtenerDato() {
        System.out.println("Datos en la Cola: ");
        for(Object x:cola){
            System.out.println(x);
        }
    }
}

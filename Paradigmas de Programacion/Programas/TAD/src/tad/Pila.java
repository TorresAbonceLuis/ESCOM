package tad;
import java.util.ArrayList;
import java.util.Stack;
public class Pila extends DatosLineales{
    Stack pila = new Stack();
    public void agregarDato(String n){
        this.pila.push(n);
        System.out.println("Se guardo el dato en la Pila");
    }
    @Override
    public void obtenerDato() {
        System.out.println("Datos en la Pila: ");
        for(Object x:pila){
            System.out.println(x);
        }
    }
}

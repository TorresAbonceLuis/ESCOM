package tad;

import java.util.ArrayList;
public class Lista extends DatosLineales{
    private final ArrayList lista1=new ArrayList();
    @Override
    public void agregarDato(String n){
        this.lista1.add(n);
        System.out.println("Se guardo el dato en la lista");
    }
    @Override
    public void obtenerDato() {
        System.out.println("Datos en la lista: ");
        for(Object x:lista1){
            System.out.println(x);
        }
    }
}

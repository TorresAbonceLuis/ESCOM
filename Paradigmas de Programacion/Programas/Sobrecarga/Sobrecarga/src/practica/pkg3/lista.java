package practica.pkg3;

import java.util.Arrays;

public class lista {
    private String cadena[];
    private int tamanio = 0;
    public void add(String texto){
        String aux[];
        aux=Arrays.copyOf(this.cadena, this.tamanio);
        this.tamanio++;
        this.cadena = new String[this.tamanio];
        System.arraycopy(aux, 0, this.cadena, 0, aux.length);
        this.cadena[tamanio-1] = texto;
    }
    
    public lista() {
        this.cadena = new String[this.tamanio];
    }
 
    public String[] getCadena() {
        return cadena;
    }
    
    public void add(int posicion,String texto){
        String auxCadena[];
        String auxCadena1[];
        auxCadena = Arrays.copyOf(this.cadena, posicion);
        auxCadena1= Arrays.copyOfRange(this.cadena, posicion, this.tamanio);
        this.tamanio++;
        this.cadena = new String[this.tamanio];
        System.arraycopy(auxCadena, 0, this.cadena, 0, auxCadena.length);
        this.cadena[posicion] = texto;
        this.tamanio+=auxCadena1.length-1;
        System.arraycopy(auxCadena1, 0, this.cadena, posicion+1, auxCadena1.length);
    }
}

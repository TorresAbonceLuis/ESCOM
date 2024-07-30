package carro;
import java.util.ArrayList;
public class Carro {
    public static void main(String[] args) {
        ArrayList <Cliente> Clientes = new ArrayList (); 
        ArrayList <Carro> Carritos = new ArrayList (); 
        ArrayList <Producto> Catalogo = new ArrayList ();
        Cliente c1 =new Cliente();
        Cliente c2 =new Cliente();
        Cliente c3 =new Cliente();
        c1.setNombre("Luis Torres"); c1.setCorreo("luis@gmail.com");
        c2.setNombre("Jose Jimenez"); c2.setCorreo("jose@gmail.com");
        c3.setNombre("Sebastian Garcia"); c3.setCorreo("sebastian@gmail.com");
        Clientes.add(c1); Clientes.add(c2); Clientes.add(c3);
        System.out.println("Menu Principal"); System.out.println("Bienvenido a ESCOMazon");
        int i=0;
        while(i!=Clientes.size()){
            System.out.print("Cliente #"+(i+1)+" ");
            System.out.println(Clientes.get(i).getNombre());
            i++;
        }
    }
}

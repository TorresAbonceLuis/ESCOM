
package carritodecompras;

import java.util.ArrayList;
import javax.swing.JOptionPane;

/**
 *
 * @author AleBe
 */
public class Carrito {
    static int Gen_id=0;
    private int ID;
    private Cliente cliente;
    private ArrayList <Item> Articulos = new ArrayList();

    public Carrito() {
        ID=Gen_id++; // Incremental
    }
        
    public void asignarCliente(Cliente c){
        cliente=c;
    }
    public void agregar(Producto P, int cantidad){
       
       Item I;
       P.set_stock(P.get_stock()-cantidad); // Se estan apartando
       //buscar si el producto esta ya en el carro
       for(int i=0;i<Articulos.size();i++)
        { I=Articulos.get(i);
          if(I.get_prod().equals( P ))
          { 
             I.set_can(I.get_can()+cantidad);
             return;
          } 
        }    
        // De lo contrario se crea el Item y se hace las conexiones     
        I=new Item(P,cantidad);
        I.AsignarCarro( this );
        Articulos.add(I);   
      }
    
    public String checkout (){
     if(!Articulos.isEmpty()){
        // Generar el ticket
        String ticket=""; 
        float Total=0.0f,precio,Sub;
        int Uni;
        for (Item I : Articulos){
            Uni=I.get_can();
            precio=I.get_prod().get_prec();
            Sub=precio*Uni;
            ticket+=I.get_prod().get_nom()+" Unidades: "+ Uni +" precio unitario: "+ precio + " Subtotal: " + Sub + "\n";
            Total+=Sub;            
        }
        ticket+="Total = "+ Total;  
        // Vaciar el carrito
        Articulos.clear();
        return ticket;
      } 
      return "Carro Vacio";
    }

    public int get_ID() {
        return ID;
    }
    
    public int get_cant(){
        int a=0;
        for(Item I : Articulos){
            a += I.get_can();
        }
        return a;
    }
    public int get_tam(){
        return Articulos.size();
    }
    public Item get_art(int opc){
        return Articulos.get(opc);
    }
    public void quitar(int opc){
        // Regresar los productos apartados al momento de quitarlo del carro
        Producto P= Articulos.get(opc).get_prod(); 
        int NumPro = Articulos.get(opc).get_can();
        int cant=P.get_stock();
        P.set_stock(cant+NumPro);
        Articulos.remove(opc);   
    }
    public void vaciar(){
        for(int i=0;i<Articulos.size();i++)
             quitar(i);
    }
}

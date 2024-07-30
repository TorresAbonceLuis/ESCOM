package asociación;
import java.util.ArrayList;


public class Cuenta {
    public ArrayList <Cliente> getTitulares() {return titulares;}
    public int getNumeroC() {return numeroC;}
    public void setNumeroC(int numeroC) {}
    private ArrayList <Cliente> titulares;
    private int numeroC;
    
    public Cuenta(int num){
        numeroC=num;
        titulares=new ArrayList();
    }
    public void agregarclient(Cliente c){
        titulares.add(c);
    }
}

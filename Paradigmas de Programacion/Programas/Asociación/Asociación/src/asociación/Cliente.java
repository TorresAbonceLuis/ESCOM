package asociación;
import java.util.ArrayList;
public class Cliente {
    public ArrayList<Cuenta> getCuenta() {return cuenta;}
    public String getNombre() {return nombre;}
    
    private String nombre;
    private String telefono;
    private String correoE;
    private ArrayList<Cuenta> cuenta;
    
    public Cliente(String nom,String tel,String correo){
        nombre=nom;
        telefono=tel;
        correoE=correo;
        cuenta=new ArrayList();
    }
    public void asignarCuenta(Cuenta cuent){
        getCuenta().add(cuent);
        cuent.agregarclient(this);
    }
}

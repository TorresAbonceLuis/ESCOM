package asociación; 
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Asociación {
    public static void main(String[] args) throws IOException {
        ArrayList <Cuenta> cuenta = new ArrayList();
        ArrayList <Cliente> cliente = new ArrayList();
        //Agregamos todos los clientes y las cuentes
        cliente.add(new Cliente("Lorea","5584162745","lorea@gmail.com"));
        cliente.add(new Cliente("Maribel","551234567","maribel@gmail.com"));
        cliente.add(new Cliente("Mario","5598776543","mario@gmail.com"));
        cuenta.add(new Cuenta(123));
        cuenta.add(new Cuenta(456));
        cuenta.add(new Cuenta(789));
        //Asignamos los clientes a las respectivas cuentas
        cliente.get(0).asignarCuenta(cuenta.get(0));
        cliente.get(0).asignarCuenta(cuenta.get(2));
        cliente.get(1).asignarCuenta(cuenta.get(1));
        cliente.get(1).asignarCuenta(cuenta.get(0));
        cliente.get(2).asignarCuenta(cuenta.get(1));
        //Menu del programa
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int opcion1=0;
        while(opcion1!=1){
            System.out.println("\tMenu del programa");
            System.out.println("1. Mostrar todos los clientes");
            System.out.println("2. Salir del programa");
            System.out.print("Seleccione una opcion: ");
            String opcion=br.readLine();
            opcion1=Integer.parseInt(opcion);
            switch(opcion1){
                case 1:
                    int i=1;
                    for(Cliente clien : cliente){
                        System.out.println(i+". "+clien.getNombre());
                        i++;
                    }
                    System.out.print("Selecciona un cliente: ");
                    String x =br.readLine();
                    int y=Integer.parseInt(x);
                    y--;
                    System.out.println("El cliente "+cliente.get(y).getNombre()+" tiene asociadas las siguientes cuentas:");
                    for(int j=0,k=1;j<cliente.get(y).getCuenta().size();j++,k++){
                        System.out.println(k+". "+cliente.get(y).getCuenta().get(j).getNumeroC());
                    }
                    break;
                case 2:
                    System.exit(0);
                default:
                    System.out.println("Seleccione una opcion valida");
            }
        }
    }
}
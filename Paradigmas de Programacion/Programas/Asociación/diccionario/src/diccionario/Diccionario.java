package diccionario;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Diccionario {
    public static void main(String[] args) throws IOException {
        boolean i;
        BufferedReader bufer = new BufferedReader(new InputStreamReader(System.in));
        i=false;
        int opcion;
        while(i!=true){
            System.out.println("Menu del diccionario");
            System.out.println("1. Agregar palabra (con definicion y sinonimo)");
            System.out.println("2. Buscar definicion de palabra");
            System.out.println("3. Serializar diccionario");
            System.out.println("4. Deserelizar diccionario");
            System.out.println("5. Salir");
            System.out.print("Selecciona una opcion: ");
            try{
                opcion=Integer.parseInt(bufer.readLine());
            }
            catch(Exception e){
                opcion=10;
            }
            switch(opcion){
                case 1:
                    break;
                case 2:
                    break;
                case 3:
                    break;    
                case 4:
                    break;
                case 5:
                    System.exit(0);
                default:
                    System.out.println("Introduce una opcion valida");
            }
                    
        }
    }
}

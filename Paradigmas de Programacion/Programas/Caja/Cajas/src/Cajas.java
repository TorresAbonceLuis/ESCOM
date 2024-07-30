import java.awt.Component;
import javax.swing.JOptionPane;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Cajas {

    /**
     *
     * @param args
     * @throws java.io.IOException
     */
    public static void main(String[] args) throws IOException {
        String menu=null;
        int opcion=1;
        while(opcion==1){
            while(menu==null){
                try{
                    menu = JOptionPane.showInputDialog("Menu"+"\n"+"1.Convertir Farenheit a Celsius"+"\n"+
                    "2.Convertir Pesos a Dolares"+"\n"+"3.Convertir Pulgadas a Centimetros"+"\n"+"4.Salir");
                    opcion =Integer.parseInt(menu);
                }
                catch(Exception e){
                    JOptionPane.showMessageDialog(null, "Inserta un valor Valido");
                    menu=null;
                }
            }
            switch(opcion){
                case 1:
                    String temperatura;
                    try{
                        temperatura =JOptionPane.showInputDialog("Convertir Farenheit a Celsius"+"\n"+"Farenheit a Convertir");
                        int conversionTemp=Integer.parseInt(temperatura);
                        int resultadoTemp=(conversionTemp-30)/2;
                        JOptionPane.showMessageDialog(null, resultadoTemp+"°");
                        opcion=1;
                        menu=null;
                        break;
                    }
                    catch(Exception e){
                       JOptionPane.showMessageDialog(null, "Inserta un valor Valido");
                       menu=null;
                       opcion=1;
                       break;
                    }
                case 2:
                    String dinero;
                    try{
                        dinero=JOptionPane.showInputDialog("Convertir Pesos a Dolares"+"\n"+"Pesos a Convertir");
                        int conversionDin=Integer.parseInt(dinero);
                        double resultadoDin=conversionDin*0.049;
                        JOptionPane.showMessageDialog(null,"$"+resultadoDin);   
                        opcion=1;
                        menu=null;
                        break;
                    }
                    catch(Exception e){
                       JOptionPane.showMessageDialog(null, "Inserta un valor Valido");
                       menu=null;
                       opcion=1;
                       break;
                    }
                case 3:
                    String distancia;
                    try{
                        distancia=JOptionPane.showInputDialog("Convertir Pulgadas a Centimetros"+"\n"+"Pulgadaa a Convertir");
                        int conversionDis=Integer.parseInt(distancia);
                        double resultadoDis=conversionDis*2.54;
                        JOptionPane.showMessageDialog(null,resultadoDis+"cm");   
                        opcion=1;
                        menu=null;
                        break;
                    }
                    catch(Exception e){
                       JOptionPane.showMessageDialog(null, "Inserta un valor Valido");
                       menu=null;
                       opcion=1;
                       break;
                    }
                case 4:
                    opcion=0;
                break;
                default:
                    System.out.println("Selecciona una opcion valida");
            }
        }
    }
}
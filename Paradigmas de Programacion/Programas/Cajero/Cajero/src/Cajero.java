import javax.swing.JOptionPane;
/**
 *
 * @author luism
 */
public class Cajero {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Cuenta cuenta1 =  new Cuenta();
        cuenta1.Nombre="Luis Torres";
        cuenta1.direccion="Escom Salon B2";
        int opcion=5;
        String menu=null;
        while(menu==null){
            try{
                menu=JOptionPane.showInputDialog("Menu del Banco"+"\n"+"\t"+
                                                "Nombre: "+cuenta1.Nombre+"\n"+"Direccion: "+cuenta1.direccion+"\n"+
                                                "1.Ver Saldo"+"\n"+
                                                "2.Depositar Una Cantidad"+"\n"+
                                                "3.Retirar Una Cantidad"+"\n"+
                                                "4.Salir"+"\n");
                opcion=Integer.parseInt(menu);
            }
            catch(Exception e){
                JOptionPane.showMessageDialog(null, "Selecciona una Opcion Correcta");
                menu=null;
                opcion=5;
            }
            switch(opcion){
                case 1:
                    cuenta1.verSaldo();
                    menu =null;
                break;
                case 2:
                    cuenta1.depositar();
                    menu =null;
                break;
                case 3:
                    cuenta1.Retirar();
                    menu =null;
                break;
                case 4:
                    JOptionPane.showMessageDialog(null, "Adios Vuelva pronto");
                    menu="1";
                break;
                default:
            }
        }
    }
}
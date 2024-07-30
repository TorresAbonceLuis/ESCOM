import javax.swing.JOptionPane;
/**
 *
 * @author brayan
 */
public class Cajero {
    public static void main(String[] args) {
        int opc=0;
        Cuenta cuenta =  new Cuenta();
        String menu=null;
        while(menu==null){
            try{
                menu=JOptionPane.showInputDialog("Menu"+"\n"+
                                                "1.Ver Saldo"+"\n"+
                                                "2.Depositar una Cantidad"+"\n"+
                                                "3.Retirar una Cantidad"+"\n"+
                                                "4.Salir"+"\n");
                opc=Integer.parseInt(menu);
            }
            catch(Exception e){
                JOptionPane.showMessageDialog(null, "Selecciona una Opcion Correcta");
                menu=null;
                opc=5;
            }
            switch(opc){
                case 1:
                    cuenta.verSaldo();
                    menu =null;
                    break;
                case 2:
                    cuenta.depositar();
                    menu =null;
                    break;
                case 3:
                    cuenta.Retirar();
                    menu =null;
                    break;
                case 4:
                    System.exit(0);
            }
        }
    }
}
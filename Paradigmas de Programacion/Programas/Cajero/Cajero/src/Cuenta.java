import javax.swing.JOptionPane;
/**
 *
 * @author luism
 */
public class Cuenta {
    double saldo=1500;
    double comision=30.50;
    String Nombre;
    String direccion;
    public void verSaldo(){
        if(saldo<1000){
            saldo=saldo-comision;
            JOptionPane.showMessageDialog(null,"Saldo de: $"+ saldo+"Se ha cobrado comision");
        }else
            JOptionPane.showMessageDialog(null, "Saldo de: $"+saldo);
    }
    public void depositar(){
        int x=1;
        while(x==1){
            try{
                String deposito =JOptionPane.showInputDialog(null,"Cantidad a Depositar");
                if(deposito==null){
                    JOptionPane.showMessageDialog(null, "Se regresara al menu","Advertencia",JOptionPane.WARNING_MESSAGE);
                    x=0;
                }else{
                    int depositoN = Integer.parseInt(deposito);
                    saldo=saldo+depositoN;
                    JOptionPane.showMessageDialog(null, "Se deposito la cantidad de: "+"$"+depositoN);
                    x=0;
                }
            }
            catch(Exception e){
                JOptionPane.showMessageDialog(null, "Introduce una Cantidad valida");
            }
        }
    }
    public void Retirar(){
        if(saldo>0){
            int x=1;
            while(x==1){
                try{
                    String retirar = JOptionPane.showInputDialog(null,"Cantidad a retirar");
                    if(retirar==null){
                        JOptionPane.showMessageDialog(null, "Se regresara al menu","Advertencia",JOptionPane.WARNING_MESSAGE);
                        x=0;
                    }else{
                        double retirarN=Double.parseDouble(retirar);
                        if(retirarN>0){
                            if(saldo<1000){
                                if(saldo>=retirarN+comision){
                                    saldo=saldo-(retirarN+comision);
                                    JOptionPane.showMessageDialog(null, "Se ha retirado la cantidad de: "+"$"+retirarN+" mas la comision");
                                    x=0;
                                }else{
                                    JOptionPane.showMessageDialog(null, "Saldo Insuficiente");
                                    x=0;
                                }
                            }else{
                                if(saldo>=retirarN){
                                    JOptionPane.showMessageDialog(null, "Se ha retirado la cantidad de: "+"$"+retirarN);
                                    saldo=saldo-retirarN;
                                    x=0;
                                }else{
                                    JOptionPane.showMessageDialog(null, "Saldo Insuficiente");
                                    x=0;
                                }
                            }
                        }else{
                            JOptionPane.showMessageDialog(null, "Retiro invalido");
                            x=0;
                        }
                    }
                }
                catch(Exception e){
                    JOptionPane.showMessageDialog(null, "Introduce una cantidad valida");
                    x=1;
                }
            }
        }else
            JOptionPane.showMessageDialog(null, "Saldo insuficiente");
    }
}

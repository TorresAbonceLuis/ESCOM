package clasefraccion;
public class ClaseFraccion {
    public static void main(String[] args) {
        Fraccion F1=new Fraccion();
        Fraccion F2=new Fraccion();
        F1.num=1;
        F1.den =3;
        F2.num=1;
        F2.den=2;
        Fraccion F = new Fraccion();
        F=F1.sumar(F2);
        System.out.println(F1.toString()+" + "+F1.toString()+" = "+F.toString());
        System.out.println(F1.toString());
        System.out.println(F2.toString());
        System.out.println(F.toString());
    }   
}
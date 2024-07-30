package clasefraccion;
public class Fraccion {
    int num;
    int den;
    public Fraccion sumar(Fraccion F2){
        Fraccion respuesta = new Fraccion();
        respuesta.den= den*F2.den;
        respuesta.num=num*F2.den+F2.num*den;
        respuesta = simplificar(respuesta);
        return respuesta;
    }
    public Fraccion simplificar(Fraccion F){
        int menor,mayor,mcd=0,i;
        if (F.den==1||F.num==1 )  
            return F;
        if (F.den == F.num){
            F.den = F.num=1;  
            return F;                
        }
        if (F.den < F.num){
            menor=F.den;
            mayor=F.num;
        }else{
            menor=F.num;
            mayor=F.den;  
        }
        if (mayor%menor==0){
            F.num= F.num / menor;  
            F.den=F.den/menor;
            return F;
        }
        for (i=1;i<menor;i++)
            if (F.num%i==0&&F.den%i==0)
             mcd=i;
        F.num=F.num/mcd;  
        F.den=F.den/mcd;
        return F;
    }
    @Override
    public String toString(){
        String nu=Integer.toString(num);
        String de=Integer.toString(den);
        String F = nu+"/"+de;
        return F;
    }
}
 

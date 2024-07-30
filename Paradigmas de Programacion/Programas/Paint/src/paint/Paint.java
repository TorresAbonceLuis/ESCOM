package paint;
import java.util.ArrayList;
public class Paint {
    public static void main(String[] args) {
        ArrayList <FigurasGeometricas> Figuras = new ArrayList();
        Figuras.add(new Circulo());
        Figuras.add(new Triangulo());
        Figuras.add(new Cuadrado());
        Figuras.add(new Triangulo());
        Figuras.add(new Cuadrado());
        for (FigurasGeometricas x :Figuras)
            x.DibujarFigura();
    }
}

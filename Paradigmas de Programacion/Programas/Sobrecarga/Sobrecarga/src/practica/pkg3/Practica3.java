package practica.pkg3;
public class Practica3 {
    public static void main(String[] args) {
        lista palabras = new lista();
        palabras.add("Chelas");
        palabras.add("Tacos");
        palabras.add(1, "huaraches");
        palabras.add("sopes");
        palabras.add(2,"Pulque");
        System.out.println(palabras.getCadena()[0]+palabras.getCadena()[1]+palabras.getCadena()[2]+palabras.getCadena()[3]+palabras.getCadena()[4]);
    }
}

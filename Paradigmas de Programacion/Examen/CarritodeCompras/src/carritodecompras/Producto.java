/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package carritodecompras;

/**
 *
 * @author AleBe
 */
public class Producto {
    private byte ID;
    private String nombre;
    private float precio;
    private String descripcion;
    private int stock;
    
    public Producto(byte id, String n, float p, String d, int stk){
        ID=id;
        nombre = n;
        precio = p;
        descripcion = d;
        stock = stk;
    }
    public void set_stock(int disponible){
        stock = disponible;
    }
    public int get_stock(){
        return stock;
    }
    
    public String get_nom(){
        return nombre;
    }
    
    public byte get_id(){
        return ID;
    }
    
    public float get_prec(){
        return precio;
    }
    
    public String get_des(){
        return descripcion;
    }
    // @Redefiniendo el metodo toString
    public String toString (){
         String p=null;
          
         p= "Producto: " + descripcion + " precio: "+ precio + " Stock: "+ stock;
         return p;
    }
}

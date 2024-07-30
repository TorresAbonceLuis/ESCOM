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
public class Cliente {
    private byte ID;
    private String nombre;
    private float saldo;
    private Carrito carroAsignado;
    
    public Cliente(byte ID, String nombre, float saldo){
        this.ID = ID;
        this.nombre = nombre;
        this.saldo = saldo;
    }
    
    public void asignarCarrito(Carrito c){
        carroAsignado= c;
        c.asignarCliente(this);
    }
    
    public String get_nom(){
        return nombre;
    }
    
    public Carrito get_car(){
        return carroAsignado;
    }
    
}

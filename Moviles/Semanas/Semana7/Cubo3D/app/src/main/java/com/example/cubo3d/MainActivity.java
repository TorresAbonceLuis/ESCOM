package com.example.cubo3d;

import android.app.Activity;
import android.opengl.GLSurfaceView;
import android.os.Bundle;
import android.view.MotionEvent;

public class MainActivity extends Activity {
    private GLSurfaceView glsv;
    private Renderizador renderizador;

    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        glsv = new GLSurfaceView(this);
        renderizador = new Renderizador(this);
        renderizador.setScreenSize(glsv.getWidth(), glsv.getHeight());  // Establece el tamaño de la pantalla
        glsv.setRenderer(renderizador);
        this.setContentView(glsv);
    }


    @Override
    public boolean onTouchEvent(MotionEvent event) {
        switch (event.getAction()) {
            case MotionEvent.ACTION_DOWN:
                // Inicia el giro cuando se toca la pantalla
                renderizador.startRotation();
                break;

            case MotionEvent.ACTION_UP:
                // Detiene el giro cuando se levanta el dedo de la pantalla
                renderizador.stopRotation();

                // Obtén las coordenadas del toque
                float x = event.getX();
                float y = event.getY();

                // Detecta la cara seleccionada y muestra el mensaje Toast
                renderizador.detectarCaraAlFrente();
                break;
        }
        return true;
    }

    @Override
    protected void onPause() {
        super.onPause();
        glsv.onPause();
    }

    @Override
    protected void onResume() {
        super.onResume();
        glsv.onResume();
    }
}

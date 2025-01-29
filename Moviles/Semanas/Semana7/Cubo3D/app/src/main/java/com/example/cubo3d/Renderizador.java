package com.example.cubo3d;
import javax.microedition.khronos.egl.*;
import javax.microedition.khronos.opengles.*;
import android.content.*;
import android.opengl.GLSurfaceView;
import android.opengl.GLU;
import javax.microedition.khronos.egl.*;
import javax.microedition.khronos.opengles.*;
import android.content.*;
import android.opengl.GLSurfaceView;
import android.opengl.GLU;
import android.widget.Toast;
import android.opengl.Matrix;



class Renderizador implements GLSurfaceView.Renderer {
    private MiCubo mc;
    private static float angulo = 0, velocidad = 1.7f;
    private float currentAngle = 0;  // Nuevo: ángulo actual
    private boolean isRotating = false;  // Variable para controlar el estado del giro
    private Context mContext;  // Agrega esta variable

    public Renderizador(Context cx) {
        mc = new MiCubo(cx);
        mContext = cx;  // Inicializa mContext con el contexto proporcionado
    }
    @Override
    public void onSurfaceCreated(GL10 gl, EGLConfig eglc) {
        gl.glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
        gl.glClearDepthf(1.0f);
        gl.glEnable(GL10.GL_DEPTH_TEST);
        gl.glDepthFunc(GL10.GL_LEQUAL);
        gl.glHint(GL10.GL_PERSPECTIVE_CORRECTION_HINT, GL10.GL_NICEST);
        gl.glShadeModel(GL10.GL_SMOOTH);
        gl.glDisable(GL10.GL_DITHER);
        mc.loadTexture(gl);
        gl.glEnable(GL10.GL_TEXTURE_2D);
    }
    @Override
    public void onSurfaceChanged(GL10 gl, int w, int h) {
        if (h == 0) h = 1;
        float spct = (float) w/h;
        gl.glViewport(0, 0, w, h);
        gl.glMatrixMode(GL10.GL_PROJECTION);
        gl.glLoadIdentity();
        GLU.gluPerspective(gl, 45, spct, 0.1f, 100.f);
        gl.glMatrixMode(GL10.GL_MODELVIEW);
        gl.glLoadIdentity();

        // Establece el tamaño de la pantalla en el Renderizador
        setScreenSize(w, h);
    }

    private int screenWidth;
    private int screenHeight;

    // Método para establecer el tamaño de la pantalla
    public void setScreenSize(int width, int height) {
        screenWidth = width;
        screenHeight = height;
    }


    // Método para iniciar el giro manualmente
    public void startRotation() {
        isRotating = true;
    }

    // Método para detener el giro manualmente y mantener el ángulo actual
    public void stopRotation() {
        isRotating = false;
        currentAngle = angulo;
    }

    @Override
    public void onDrawFrame(GL10 gl) {
        gl.glClear(GL10.GL_COLOR_BUFFER_BIT | GL10.GL_DEPTH_BUFFER_BIT);
        gl.glLoadIdentity();
        gl.glTranslatef(0.0f, 0.0f, -6.0f);

        if (isRotating) {
            gl.glRotatef(angulo, 0.15f, 1.0f, 0.3f);
            angulo += velocidad;
        } else {
            gl.glRotatef(currentAngle, 0.15f, 1.0f, 0.3f);
        }

        mc.draw(gl);
    }


    // Método para establecer el tamaño de la pantalla

    public int detectarCaraAlFrente() {
        // Define un vector que representa la dirección de la vista
        float[] viewVector = {0, 0, -1, 0};

        // Aplica la rotación actual al vector de la vista
        float[] rotationMatrix = new float[16];
        Matrix.setIdentityM(rotationMatrix, 0);
        Matrix.rotateM(rotationMatrix, 0, currentAngle, 0.15f, 1.0f, 0.3f);
        Matrix.multiplyMV(viewVector, 0, rotationMatrix, 0, viewVector, 0);

        // Determina la cara basándote en la dirección de la vista
        int caraSeleccionada = -1;
        float maxDotProduct = -1;  // Inicializa el producto punto máximo

        for (int i = 0; i < 6; i++) {
            float[] normalVector = calcularVectorNormalCara(i);

            // Calcula el producto punto entre el vector de vista y el vector normal de la cara
            float dotProduct = dotProduct(viewVector, normalVector);

            // Si el producto punto es el más grande hasta ahora, actualiza la cara seleccionada
            if (dotProduct > maxDotProduct) {
                maxDotProduct = dotProduct;
                caraSeleccionada = i;
            }
        }

        // Muestra el mensaje Toast con el nombre de la cara seleccionada
        mostrarMensajeCaraSeleccionada(caraSeleccionada);

        return caraSeleccionada;
    }

    // Método para calcular el producto punto entre dos vectores tridimensionales
    private float dotProduct(float[] vector1, float[] vector2) {
        return vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2];
    }

    // Método para calcular el vector normal de una cara específica
    private float[] calcularVectorNormalCara(int cara) {
        float[] normal = new float[3];

        switch (cara) {
            case 0:  // Frente
                normal[0] = 0; normal[1] = 1; normal[2] = 0;
                break;
            case 1:  // Derecha
                normal[0] = 1; normal[1] = 0; normal[2] = 0;
                break;
            case 2:  // Tope
                normal[0] = 0; normal[1] = 0; normal[2] = 1;
                break;
            case 3:  // Base
                normal[0] = 0; normal[1] = -1; normal[2] = 0;
                break;
            case 4:  // Izquierda
                normal[0] = -1; normal[1] = 0; normal[2] = 0;
                break;
            case 5:  // Atrás
                normal[0] = 0; normal[1] = 0; normal[2] = -1;
                break;
        }

        return normal;
    }


    // Método para mostrar el Toast con el nombre de la cara seleccionada
    private void mostrarMensajeCaraSeleccionada(int caraSeleccionada) {
        String nombreCara = mc.obtenerNombreCara(caraSeleccionada);
        String mensaje = "Cara seleccionada: " + nombreCara;
        Toast.makeText(mContext, mensaje, Toast.LENGTH_SHORT).show();
    }
}


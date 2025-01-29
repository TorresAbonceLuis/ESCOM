package com.example.orientacion;

import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity implements SensorEventListener, SurfaceHolder.Callback {

    private SensorManager sensorManager;
    private Sensor accelerometer, magnetometer;
    private TextView accelerationTextView;
    private SurfaceView compassSurfaceView;
    private SurfaceHolder surfaceHolder;
    private Paint paint;
    private float[] gravity = new float[3];
    private float[] geomagnetic = new float[3];
    private float[] rMat = new float[9];
    private float[] iMat = new float[9];
    private float[] orientation = new float[3];
    private float azimuth = 0;
    private float northAngle = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        accelerationTextView = findViewById(R.id.acceleration);
        compassSurfaceView = findViewById(R.id.compassSurfaceView);
        surfaceHolder = compassSurfaceView.getHolder();
        surfaceHolder.addCallback(this);

        paint = new Paint();
        paint.setAntiAlias(true);
        paint.setStyle(Paint.Style.STROKE);
        paint.setStrokeWidth(5);
        paint.setColor(Color.BLACK);

        sensorManager = (SensorManager) getSystemService(SENSOR_SERVICE);
        accelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        magnetometer = sensorManager.getDefaultSensor(Sensor.TYPE_MAGNETIC_FIELD);

        sensorManager.registerListener(this, accelerometer, SensorManager.SENSOR_DELAY_UI);
        sensorManager.registerListener(this, magnetometer, SensorManager.SENSOR_DELAY_UI);
    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        if (event.sensor.getType() == Sensor.TYPE_ACCELEROMETER) {
            System.arraycopy(event.values, 0, gravity, 0, event.values.length);
        } else if (event.sensor.getType() == Sensor.TYPE_MAGNETIC_FIELD) {
            System.arraycopy(event.values, 0, geomagnetic, 0, event.values.length);
        }

        if (gravity != null && geomagnetic != null) {
            if (SensorManager.getRotationMatrix(rMat, iMat, gravity, geomagnetic)) {
                SensorManager.getOrientation(rMat, orientation);
                azimuth = (float) Math.toDegrees(orientation[0]);
                if (azimuth < 0) {
                    azimuth += 360;
                }
                northAngle = -azimuth; // Invert the angle to point the arrow correctly
                if (northAngle < 0) {
                    northAngle += 360;
                }
                drawCompass();
            }
        }

        // Calculate the acceleration without gravity
        float acceleration = (float) Math.sqrt(Math.pow(gravity[0], 2) + Math.pow(gravity[1], 2) + Math.pow(gravity[2], 2));
        accelerationTextView.setText("Acceleration: " + (acceleration - SensorManager.GRAVITY_EARTH) + " m/s²");
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {
        // Do nothing for now
    }

    @Override
    protected void onResume() {
        super.onResume();
        sensorManager.registerListener(this, accelerometer, SensorManager.SENSOR_DELAY_UI);
        sensorManager.registerListener(this, magnetometer, SensorManager.SENSOR_DELAY_UI);
    }

    @Override
    protected void onPause() {
        super.onPause();
        sensorManager.unregisterListener(this, accelerometer);
        sensorManager.unregisterListener(this, magnetometer);
    }

    @Override
    public void surfaceCreated(SurfaceHolder holder) {
        drawCompass(); // Draw the compass when the surface is created
    }

    @Override
    public void surfaceChanged(SurfaceHolder holder, int format, int width, int height) {
        drawCompass(); // Redraw the compass when the surface changes
    }

    @Override
    public void surfaceDestroyed(SurfaceHolder holder) {
        // Do nothing for now
    }

    private void drawCompass() {
        Canvas canvas = surfaceHolder.lockCanvas();
        if (canvas != null) {
            canvas.drawColor(Color.WHITE);

            int width = canvas.getWidth();
            int height = canvas.getHeight();
            int centerX = width / 2;
            int centerY = height / 2;
            int radius = Math.min(centerX, centerY) - 10;

            // Draw the compass circle
            paint.setColor(Color.BLACK);
            paint.setStyle(Paint.Style.STROKE);
            canvas.drawCircle(centerX, centerY, radius, paint);

            // Draw the N, S, E, W letters
            paint.setTextSize(40);
            paint.setStyle(Paint.Style.FILL);
            canvas.drawText("N", centerX - 10, centerY - radius + 40, paint);
            canvas.drawText("S", centerX - 10, centerY + radius - 10, paint);
            canvas.drawText("E", centerX + radius - 40, centerY + 10, paint);
            canvas.drawText("W", centerX - radius + 10, centerY + 10, paint);


            // Ajustar un pequeño offset al ángulo de la brújula para mover la flecha a la izquierda
            float offsetAngle = 5; // Cambia este valor según sea necesario para ajustar la posición de la flecha
            float adjustedAngle = northAngle + offsetAngle;

            // Rotate
            // Rotate the canvas to draw the rotated arrow pointing north
            canvas.save();
            canvas.rotate(adjustedAngle, centerX, centerY);

            // Draw the rotated arrow pointing north
            paint.setColor(Color.BLUE);
            paint.setStrokeWidth(8);
            canvas.drawLine(centerX, centerY - radius + 20, centerX, centerY + radius - 20, paint);
            canvas.drawLine(centerX, centerY - radius + 20, centerX - 20, centerY - radius + 60, paint);
            canvas.drawLine(centerX, centerY - radius + 20, centerX + 20, centerY - radius + 60, paint);

            canvas.restore();
            surfaceHolder.unlockCanvasAndPost(canvas);
        }
    }
}

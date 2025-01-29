package com.example.preferencias;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.app.Activity;
import android.widget.*;
import android.graphics.*;
import android.net.Uri;

import java.io.InputStream;

public class MainActivity extends Activity {
    SharedPreferences sp;
    EditText jetn, jetx, jety;
    String s;
    float x, y;
    ImageView imageView;

    // Identificador para la selección de imagen desde la galería
    private static final int PICK_IMAGE = 1;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        jetn = findViewById(R.id.xetn);
        jetx = findViewById(R.id.xetx);
        jety = findViewById(R.id.xety);
        sp = getSharedPreferences("preferencias", Context.MODE_PRIVATE);
        s = sp.getString("titulo", "ESCOM");
        x = sp.getFloat("x", 0);
        y = sp.getFloat("y", 0);
        jetn.setText(s);
        jetx.setText(String.valueOf(x));
        jety.setText(String.valueOf(y));

        imageView = findViewById(R.id.imageView);

        // Botón para seleccionar imagen desde la galería
        Button selectImageButton = findViewById(R.id.select_image_button);
        selectImageButton.setOnClickListener(v -> openGallery());
    }

    @Override
    protected void onPause() {
        super.onPause();
        s = jetn.getText().toString();
        x = Float.parseFloat(jetx.getText().toString());
        y = Float.parseFloat(jety.getText().toString());
        SharedPreferences.Editor miEditor = sp.edit();
        miEditor.putString("titulo", s);
        miEditor.putFloat("x", x);
        miEditor.putFloat("y", y);
        miEditor.apply();
        Toast.makeText(this, "Preferencias guardadas", Toast.LENGTH_LONG).show();
    }

    // Método para abrir la galería y seleccionar una imagen
    private void openGallery() {
        Intent intent = new Intent();
        intent.setType("image/*");
        intent.setAction(Intent.ACTION_GET_CONTENT);
        startActivityForResult(Intent.createChooser(intent, "Select Picture"), PICK_IMAGE);
    }

    // Método para manejar el resultado de la selección de imagen
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == PICK_IMAGE && resultCode == RESULT_OK && data != null && data.getData() != null) {
            Uri uri = data.getData();
            try {
                // Cargar la imagen en un Bitmap
                InputStream inputStream = getContentResolver().openInputStream(uri);
                Bitmap bitmap = BitmapFactory.decodeStream(inputStream);
                inputStream.close();

                // Mostrar la imagen en el ImageView
                imageView.setImageBitmap(bitmap);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}

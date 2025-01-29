package com.example.proyectoparte2;

import android.os.Bundle;
import android.app.Activity;
import android.view.View;

public class pantallaProgramas extends Activity {
    private ButtonController mainButtonController;
    private ButtonController programButtonController;
    private ButtonController noiseButtonController;
    private ButtonController pitchButtonController;
    private AudioController audioController;
    private PopupController popupController;
    BluetoothConnector bluetoothConnector = BluetoothConnector.getInstance();
    private Thread blinkThread;
    private int startTime;
    private String currentProgram;
    private volatile boolean isPaused = false;
    private volatile boolean isRuido = true;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pantallaprogramas);
        mainButtonController = new ButtonController(this, R.id.volumenButton, R.id.ruidoButton, R.id.programaButton, R.id.pitchButton);
        programButtonController = new ButtonController(this, R.id.programaA0Button, R.id.programaA1Button, R.id.programaA2Button, R.id.startButton, R.id.pauseButton, R.id.resumeButton);
        noiseButtonController = new ButtonController(this, R.id.ruidoBlancoSuaveButton, R.id.tonoModuladoButton);
        pitchButtonController = new ButtonController(this, R.id.arribaButton, R.id.abajoButton);
        audioController = new AudioController(this, R.raw.a0);  // Cambiar el recurso según sea necesario
        popupController = new PopupController(this);
        configureButtonActions();
    }

    private void configureButtonActions() {
        final boolean[] areButtonsHidden = {false, false, false, false, false};

        mainButtonController.setOnClickListener(R.id.volumenButton, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!areButtonsHidden[0]) {
                    // Ocultar todos los botones excepto el botón de volumen
                    mainButtonController.setInvisibleButtons(R.id.ruidoButton, R.id.programaButton, R.id.pitchButton);
                    mainButtonController.setVisibleButtons(R.id.volumenButton);

                    // Mostrar la barra de volumen
                    popupController.showVolumePopup(v, audioController);

                    areButtonsHidden[0] = true;
                } else {
                    // Mostrar todos los botones
                    mainButtonController.setVisibility(View.VISIBLE);

                    // Ocultar la barra de volumen
                    popupController.hideVolumePopup();

                    areButtonsHidden[0] = false;
                }
            }
        });

        mainButtonController.setOnClickListener(R.id.ruidoButton, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!areButtonsHidden[1]) {
                    // Hacer invisibles todos los botones excepto los botones de ruido/tono blanco
                    mainButtonController.setInvisibleButtons(R.id.volumenButton, R.id.programaButton, R.id.pitchButton);
                    // Mostrar solo los botones de ruido/tono blanco
                    noiseButtonController.setVisibleButtons(R.id.ruidoBlancoSuaveButton, R.id.tonoModuladoButton);
                    areButtonsHidden[1] = true;
                } else {
                    // Mostrar todos los botones
                    mainButtonController.setVisibility(View.VISIBLE);
                    // Hacer invisibles los botones de ruido/tono blanco
                    noiseButtonController.setInvisibleButtons(R.id.ruidoBlancoSuaveButton, R.id.tonoModuladoButton);
                    areButtonsHidden[1] = false;
                }
            }
        });

        noiseButtonController.setOnClickListener(R.id.ruidoBlancoSuaveButton, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Cambiar el recurso de audio a ruido blanco suave
                isRuido = true;
            }
        });

        noiseButtonController.setOnClickListener(R.id.tonoModuladoButton, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Cambiar el recurso de audio a un tono modulado
                isRuido = false;
            }
        });

        mainButtonController.setOnClickListener(R.id.programaButton, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!areButtonsHidden[2]) {
                    // Hacer invisibles todos los botones excepto los botones de programa
                    mainButtonController.setInvisibleButtons(R.id.volumenButton, R.id.ruidoButton, R.id.pitchButton);
                    // Mostrar solo los botones de programa
                    programButtonController.setVisibleButtons(R.id.programaA0Button, R.id.programaA1Button, R.id.programaA2Button);
                    areButtonsHidden[2] = true;
                } else {
                    // Mostrar todos los botones
                    mainButtonController.setVisibility(View.VISIBLE);
                    // Hacer invisibles los botones de programa
                    programButtonController.setInvisibleButtons(R.id.programaA0Button, R.id.programaA1Button, R.id.programaA2Button);
                    areButtonsHidden[2] = false;
                }
            }
        });

        mainButtonController.setOnClickListener(R.id.pitchButton, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!areButtonsHidden[3]) {
                    // Hacer invisibles todos los botones excepto los botones de pitch
                    mainButtonController.setInvisibleButtons(R.id.volumenButton, R.id.ruidoButton, R.id.programaButton);
                    // Mostrar solo los botones de pitch
                    pitchButtonController.setVisibleButtons(R.id.arribaButton, R.id.abajoButton);
                    areButtonsHidden[3] = true;
                } else {
                    // Mostrar todos los botones
                    mainButtonController.setVisibility(View.VISIBLE);
                    // Hacer invisibles los botones de pitch
                    pitchButtonController.setInvisibleButtons(
                            R.id.arribaButton,
                            R.id.abajoButton
                    );
                    areButtonsHidden[3] = false;
                }
            }
        });

        pitchButtonController.setOnClickListener(R.id.arribaButton, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Implementación para el botón de arriba
            }
        });

        pitchButtonController.setOnClickListener(R.id.abajoButton, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Implementación para el botón de abajo
            }
        });

        programButtonController.setOnClickListener(R.id.programaA0Button, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!areButtonsHidden[4]) {
                    programButtonController.setVisibleButtons(R.id.startButton, R.id.pauseButton, R.id.resumeButton, R.id.programaA0Button);
                    programButtonController.setInvisibleButtons(R.id.programaA1Button, R.id.programaA2Button);
                    mainButtonController.setInvisibleButtons(R.id.programaButton); // Ocultar el botón de programa
                    areButtonsHidden[4] = true;
                } else {
                    programButtonController.setInvisibleButtons(R.id.startButton, R.id.pauseButton, R.id.resumeButton);
                    programButtonController.setVisibleButtons(R.id.programaA0Button,R.id.programaA1Button,R.id.programaA2Button); // Mostrar el botón programaA0Button
                    mainButtonController.setVisibleButtons(R.id.programaButton); // Mostrar el botón de programa
                    areButtonsHidden[4] = false;
                }
                if (!isRuido) {
                    audioController.changeAudioResource(R.raw.a0); // Cambiar el recurso de audio
                } else {
                    audioController.changeAudioResource(R.raw.ruidoblanco);
                }
                currentProgram = "A0";
            }
        });

        programButtonController.setOnClickListener(R.id.programaA1Button, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!areButtonsHidden[4]) {
                    programButtonController.setVisibleButtons(R.id.startButton, R.id.pauseButton, R.id.resumeButton, R.id.programaA1Button);
                    programButtonController.setInvisibleButtons(R.id.programaA0Button, R.id.programaA2Button);
                    mainButtonController.setInvisibleButtons(R.id.programaButton); // Ocultar el botón de programa
                    areButtonsHidden[4] = true;
                } else {
                    programButtonController.setInvisibleButtons(R.id.startButton, R.id.pauseButton, R.id.resumeButton);
                    programButtonController.setVisibleButtons(R.id.programaA0Button,R.id.programaA1Button,R.id.programaA2Button); // Mostrar el botón programaA0Button
                    mainButtonController.setVisibleButtons(R.id.programaButton); // Mostrar el botón de programa
                    areButtonsHidden[4] = false;
                }
                if (!isRuido) {
                    audioController.changeAudioResource(R.raw.a1); // Cambiar el recurso de audio
                } else {
                    audioController.changeAudioResource(R.raw.ruidoblanco); // Cambiar el recurso de audio
                }
                currentProgram = "A1";
            }
        });

        programButtonController.setOnClickListener(R.id.programaA2Button, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!areButtonsHidden[4]) {
                    programButtonController.setVisibleButtons(R.id.startButton, R.id.pauseButton, R.id.resumeButton, R.id.programaA2Button);
                    programButtonController.setInvisibleButtons(R.id.programaA0Button, R.id.programaA1Button);
                    mainButtonController.setInvisibleButtons(R.id.programaButton); // Ocultar el botón de programa
                    areButtonsHidden[4] = true;
                } else {
                    programButtonController.setInvisibleButtons(R.id.startButton, R.id.pauseButton, R.id.resumeButton);
                    programButtonController.setVisibleButtons(R.id.programaA0Button,R.id.programaA1Button,R.id.programaA2Button); // Mostrar el botón programaA0Button
                    mainButtonController.setVisibleButtons(R.id.programaButton); // Mostrar el botón de programa
                    areButtonsHidden[4] = false;
                }
                if (!isRuido) {
                    audioController.changeAudioResource(R.raw.a1); // Cambiar el recurso de audio
                } else {
                    audioController.changeAudioResource(R.raw.ruidoblanco); // Cambiar el recurso de audio
                }
                currentProgram = "A2";
            }
        });

        programButtonController.setOnClickListener(R.id.startButton, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Iniciar la reproducción del audio
                audioController.play();

                // Iniciar la secuencia de parpadeo
                if (blinkThread != null && blinkThread.isAlive()) {
                    blinkThread.interrupt(); // Interrumpe el hilo si ya está ejecutándose
                }
                startTime = 0;

                blinkThread = new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            // Ejecutar la secuencia de parpadeo
                            switch (currentProgram) {
                                case "A0":
                                    blinkSequence("A0", 20f, 4f, 10 * 60); // de 18hz a 7hz en 5 minutos
                                    blinkSequence("A0", 4f, 7f, 10 * 60); // mantener en 7hz durante 7 minutos
                                    blinkSequence("A0", 7f, 4f, 10 * 60);
                                    blinkSequence("A0", 4f, 7f, 10 * 60);
                                    blinkSequence("A0", 7f, 20f, 8 * 60);// de 7hz a 40hz en 3 minutos
                                    break;
                                case "A1":
                                    blinkSequence("A1", 16f, 4f, 10 * 60); // de 18hz a 7hz en 5 minutos
                                    blinkSequence("A1", 4f, 1f, 2 * 60); // mantener en 7hz durante 7 minutos
                                    blinkSequence("A1", 1f, 1f, 38 * 60);
                                    blinkSequence("A1", 1f, 15f, 6 * 60);
                                    break;
                                case "A2":
                                    blinkSequence("A2", 16f, 4f, 13 * 60); // de 18hz a 7hz en 5 minutos
                                    blinkSequence("A2", 4f, 7f, 7 * 60); // mantener en 7hz durante 7 minutos
                                    blinkSequence("A2", 7f, 4f, 7 * 60);
                                    blinkSequence("A2", 4f, 7f, 7* 60);
                                    blinkSequence("A2", 7f, 4f, 8 * 60);
                                    blinkSequence("A2", 4f, 6f, 10 * 60);
                                    blinkSequence("A2", 6f, 30f, 12 * 60);
                                    break;
                            }
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt(); // Restablecer el estado interrumpido
                        }
                    }
                });

                Thread amplitudeThread = new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            // Ejecutar la secuencia de amplitud
                            switch (currentProgram) {
                                case "A0":
                                    amplitudeSequence( 20, 4, 10 * 60); // de 18hz a 7hz en 5 minutos
                                    amplitudeSequence( 4, 7, 10 * 60); // mantener en 7hz durante 7 minutos
                                    amplitudeSequence( 7, 4, 10 * 60);
                                    amplitudeSequence( 4, 7, 10 * 60);
                                    amplitudeSequence( 7, 20, 8 * 60);
                                    break;
                                case "A1":
                                    amplitudeSequence( 16, 4, 10 * 60); // de 18hz a 7hz en 5 minutos
                                    amplitudeSequence( 4, 1, 2 * 60); // mantener en 7hz durante 7 minutos
                                    amplitudeSequence(1, 1, 38 * 60);
                                    amplitudeSequence( 1, 15, 6 * 60);
                                    break;
                                case "A2":
                                    amplitudeSequence( 16, 4, 13 * 60); // de 18hz a 7hz en 5 minutos
                                    amplitudeSequence( 4, 7, 7 * 60); // mantener en 7hz durante 7 minutos
                                    amplitudeSequence( 7, 4, 7 * 60);
                                    amplitudeSequence( 4, 7, 7* 60);
                                    amplitudeSequence( 7, 4, 8 * 60);
                                    amplitudeSequence( 4, 6, 10 * 60);
                                    amplitudeSequence( 6, 30, 12 * 60);
                                    break;
                            }
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt(); // Restablecer el estado interrumpido
                        }
                    }
                });

                blinkThread.start();
                amplitudeThread.start();
            }
        });

        programButtonController.setOnClickListener(R.id.pauseButton, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pausar la secuencia de parpadeo
                isPaused = true;
                //enviar 0 a arduino para detener la vibración
                bluetoothConnector.sendData("F0\n");
                // Pausar la reproducción del audio
                audioController.pause();
            }
        });

        programButtonController.setOnClickListener(R.id.resumeButton, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Reanudar la secuencia de parpadeo
                isPaused = false;
                // Reanudar la reproducción del audio
                audioController.play();
            }
        });
    }

    private void blinkSequence(String program, float startFrequency, float endFrequency, int duration) throws InterruptedException {
        float deltaFrequency = (endFrequency - startFrequency) / duration;
        for (int i = 0; i < duration; i++) {
            if (Thread.currentThread().isInterrupted()) {
                return; // Salir de la función si el hilo es interrumpido
            }
            while (isPaused) { // Si isPaused es verdadero, hacer que el hilo se duerma
                Thread.sleep(100);
            }
            float currentFrequency = startFrequency + deltaFrequency * i;
            if (program.equals("A0")) {
                if (i % 2 == 0) {
                    // Encender ambos LEDs
                    bluetoothConnector.sendData("1F" + String.valueOf(currentFrequency) + "\n");
                    bluetoothConnector.sendData("2F" + String.valueOf(currentFrequency) + "\n");
                } else {
                    // Apagar ambos LEDs
                    bluetoothConnector.sendData("1F0\n");
                    bluetoothConnector.sendData("2F0\n");
                }
            } else if (program.equals("A1")) {
                bluetoothConnector.sendData("2F0\n");
            }
            Thread.sleep(1000);
        }
    }

    private void amplitudeSequence(int startAmplitude, int endAmplitude, int duration) throws InterruptedException {
        float deltaAmplitude = (float)(endAmplitude - startAmplitude) / duration;
        for (int i = 0; i < duration; i++) {
            if (Thread.currentThread().isInterrupted()) {
                return; // Salir de la función si el hilo es interrumpido
            }
            int currentAmplitude = Math.round(startAmplitude + deltaAmplitude * i);
            // Enviar la amplitud actual a Arduino con un carácter de nueva línea
            // Para el LED 1
            bluetoothConnector.sendData("1A" + String.valueOf(currentAmplitude) + "\n");
            // Para el LED 2
            bluetoothConnector.sendData("2A" + String.valueOf(currentAmplitude) + "\n");
            Thread.sleep(1000);
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (blinkThread != null && blinkThread.isAlive()) {
            blinkThread.interrupt(); // Interrumpe el hilo al destruir la actividad
        }
        audioController.release();
    }
}

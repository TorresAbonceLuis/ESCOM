#include <SoftwareSerial.h>

// Configuración del módulo Bluetooth y pines de los LEDs
SoftwareSerial BT(0, 1); // GPIO 3 RX, GPIO 1 TX para ESP8266.
byte Led_1 = 5; // D1
byte Led_2 = 4; // D2

// Variables para el control de la señal Bluetooth y temporización
String dataBluetooth = "";
unsigned long previousMillis = 0;
int interval = 125; // Intervalo por defecto para el parpadeo
int amplitude = 255; // Amplitud por defecto (máxima)
String sequence = "23"; // Secuencia cíclica inicial
int currentIndex = 0; // Índice para la secuencia

void setup() {
    Serial.begin(9600);
    BT.begin(9600);
    pinMode(Led_1, OUTPUT);
    pinMode(Led_2, OUTPUT);
}

void loop() {
    // Procesar datos recibidos por Bluetooth
    while (BT.available()) {
        char c = BT.read();
        dataBluetooth += c; // Construye la cadena de datos
        if (c == '\n') { // Fin de línea indica el final de un mensaje
            processCommand(dataBluetooth);
            dataBluetooth = ""; // Reiniciar la cadena de datos después del procesamiento
        }
    }
    // Aplicar la secuencia LED inmediatamente si es necesario
    if (millis() - previousMillis >= interval) {
        previousMillis = millis();
        applyLEDSequence();
    }
}

void processCommand(String command) {
    char commandType = command.charAt(0);
    String commandValue = command.substring(1);

    switch(commandType) {
        case 'F': // Comando para cambiar frecuencia
            int freqValue = commandValue.toInt();
            interval = (freqValue == 0) ? 0 : 1000 / freqValue;
            break;
        case 'A': // Comando para cambiar amplitud
            amplitude = map(commandValue.toInt(), 0, 100, 0, 255);
            break;
        case 'S': // Comando para cambiar secuencia
            sequence = commandValue;
            currentIndex = 0;
            break;
    }
    applyLEDSequence(); // Aplica los cambios inmediatamente
}

void applyLEDSequence() {
    if (interval == 0) {
        digitalWrite(Led_1, LOW);
        digitalWrite(Led_2, LOW);
    } else {
        char currentStep = sequence[currentIndex % sequence.length()];
        currentIndex++;
        
        switch (currentStep) {
            case '0': // prendido 1
                analogWrite(Led_1, amplitude);
                analogWrite(Led_2, 0);
                break;
            case '1': // prendido 2
                analogWrite(Led_1, 0);
                analogWrite(Led_2, amplitude);
                break;
            case '2': // prendidos ambos
                analogWrite(Led_1, amplitude);
                analogWrite(Led_2, amplitude);
                break;
            case '3': // apagados ambos
                analogWrite(Led_1, 0);
                analogWrite(Led_2, 0);
                break;
        }
    }
}

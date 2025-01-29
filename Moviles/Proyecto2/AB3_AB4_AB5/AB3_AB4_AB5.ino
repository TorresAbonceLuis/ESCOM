int ledPin1 = 12; // Pin del primer LED
int ledPin2 = 13; // Pin del segundo LED
bool blinking = false; // Estado de parpadeo de los LEDs
bool tenHzBlinking = false; // Estado de parpadeo a 10 Hz
bool AB5 = false; // Estado de parpadeo de los LEDs
unsigned long previousMillis = 0; // Almacena el tiempo del último cambio de estado
unsigned long tenHzPreviousMillis = 0; // Almacena el tiempo del último cambio de estado para el parpadeo a 10 Hz
const long blinkInterval = 32; // Intervalo de tiempo para una frecuencia de 31 Hz (1 segundo / 31)
const long totalInterval = 20000; // Intervalo total de 10 segundos (5 segundos encendido, 5 segundos apagado)
const int intensity = 70; // Intensidad del LED en porcentaje (70% en este caso)
int blinkFrequency = 0; // Frecuencia de parpadeo actual
unsigned long intervalStartTime = 0; // Tiempo de inicio del intervalo actual
unsigned long intervalDuration = 0; // Duración del intervalo actual
const long totalOffInterval = 40000; // Intervalo total de 20 segundos apagados (20,000 ms)



void setup() {
  pinMode(ledPin1, OUTPUT);   // Configura el pin del primer LED como salida
  pinMode(ledPin2, OUTPUT);   // Configura el pin del segundo LED como salida
  
  Serial.begin(9600); // Inicializa la comunicación serial con una velocidad de 9600 baudios
}

void loop() {
  if (Serial.available() > 0) { // Si hay datos disponibles en el puerto serial
    char state = Serial.read(); // Lee el dato recibido

    if (state == '1') {          // Si el dato recibido es '1'
      blinking = true;           // Activa el parpadeo de los LEDs
      tenHzBlinking = false;     // Desactiva el parpadeo a 10 Hz
      AB5 = false;
      previousMillis = millis(); // Reinicia el tiempo para comenzar el ciclo
    } else if (state == '3') {   // Si el dato recibido es '3'
      digitalWrite(ledPin1, LOW);  // Apaga el primer LED
      digitalWrite(ledPin2, LOW);  // Apaga el segundo LED
      blinking = false;          // Desactiva el parpadeo de los LEDs
      tenHzBlinking = false;     // Desactiva el parpadeo a 10 Hz
      AB5 = false;
    } else if (state == '0') {   // Si el dato recibido es '0'
      blinking = false;         // Desactiva el parpadeo de los LEDs
      tenHzBlinking = true;     // Activa el parpadeo a 10 Hz
      AB5 = false;
      tenHzPreviousMillis = millis(); // Reinicia el tiempo para comenzar el ciclo del parpadeo a 10 Hz
    } else if (state == '2') {   // Si el dato recibido es '2'
      blinking = false;         // Desactiva el parpadeo de los LEDs
      tenHzBlinking = false;
      AB5 = true;
      tenHzPreviousMillis = millis(); // Reinicia el tiempo para comenzar el ciclo del parpadeo a 10 Hz
    }
  }

  if (AB5) {
    unsigned long currentMillis = millis();
    unsigned long elapsedTime = currentMillis - tenHzPreviousMillis; // Tiempo transcurrido desde el último cambio de estado

    // Determinar la frecuencia de parpadeo en función del tiempo transcurrido
    if (elapsedTime < 300000) { // Variación de 16 Hz a 7 Hz durante 5 minutos (300000 ms)
        int blinkFrequency = map(elapsedTime, 0, 300000, 16, 7);
        int blinkInterval = 1000 / blinkFrequency; // Calcular el intervalo de parpadeo en milisegundos
        if (currentMillis - tenHzPreviousMillis >= blinkInterval) {
            digitalWrite(ledPin1, !digitalRead(ledPin1)); // Invierte el estado del primer LED
            digitalWrite(ledPin2, !digitalRead(ledPin2)); // Invierte el estado del segundo LED
            tenHzPreviousMillis = currentMillis; // Actualiza el tiempo del último cambio de estado
        }
    } else if (elapsedTime < 900000) { // Variación de 7 Hz a 10 Hz durante 10 minutos (600000 ms)
        int blinkFrequency = map(elapsedTime - 300000, 0, 600000, 7, 10);
        int blinkInterval = 1000 / blinkFrequency; // Calcular el intervalo de parpadeo en milisegundos
        if (currentMillis - tenHzPreviousMillis >= blinkInterval) {
            digitalWrite(ledPin1, !digitalRead(ledPin1)); // Invierte el estado del primer LED
            digitalWrite(ledPin2, !digitalRead(ledPin2)); // Invierte el estado del segundo LED
            tenHzPreviousMillis = currentMillis; // Actualiza el tiempo del último cambio de estado
        }
    } else if (elapsedTime < 1200000) { // Variación de 10 Hz a 5 Hz durante 5 minutos (300000 ms)
        int blinkFrequency = map(elapsedTime - 900000, 0, 300000, 10, 5);
        int blinkInterval = 1000 / blinkFrequency; // Calcular el intervalo de parpadeo en milisegundos
        if (currentMillis - tenHzPreviousMillis >= blinkInterval) {
            digitalWrite(ledPin1, !digitalRead(ledPin1)); // Invierte el estado del primer LED
            digitalWrite(ledPin2, !digitalRead(ledPin2)); // Invierte el estado del segundo LED
            tenHzPreviousMillis = currentMillis; // Actualiza el tiempo del último cambio de estado
        }
    } else if (elapsedTime < 1500000) { // Variación de 5 Hz a 15 Hz durante 5 minutos (300000 ms)
        int blinkFrequency = map(elapsedTime - 1200000, 0, 300000, 5, 15);
        int blinkInterval = 1000 / blinkFrequency; // Calcular el intervalo de parpadeo en milisegundos
        if (currentMillis - tenHzPreviousMillis >= blinkInterval) {
            digitalWrite(ledPin1, !digitalRead(ledPin1)); // Invierte el estado del primer LED
            digitalWrite(ledPin2, !digitalRead(ledPin2)); // Invierte el estado del segundo LED
            tenHzPreviousMillis = currentMillis; // Actualiza el tiempo del último cambio de estado
        }
    } else if (elapsedTime < 1800000) { // Variación de 15 Hz a 11 Hz durante 5 minutos (300000 ms)
        int blinkFrequency = map(elapsedTime - 1500000, 0, 300000, 15, 11);
        int blinkInterval = 1000 / blinkFrequency; // Calcular el intervalo de parpadeo en milisegundos
        if (currentMillis - tenHzPreviousMillis >= blinkInterval) {
            digitalWrite(ledPin1, !digitalRead(ledPin1)); // Invierte el estado del primer LED
            digitalWrite(ledPin2, !digitalRead(ledPin2)); // Invierte el estado del segundo LED
            tenHzPreviousMillis = currentMillis; // Actualiza el tiempo del último cambio de estado
        }
    } else if (elapsedTime < 2160000) { // Variación de 11 Hz a 20 Hz durante 6 minutos (360000 ms)
        int blinkFrequency = map(elapsedTime - 1800000, 0, 360000, 11, 20);
        int blinkInterval = 1000 / blinkFrequency; // Calcular el intervalo de parpadeo en milisegundos
        if (currentMillis - tenHzPreviousMillis >= blinkInterval) {
            digitalWrite(ledPin1, !digitalRead(ledPin1)); // Invierte el estado del primer LED
            digitalWrite(ledPin2, !digitalRead(ledPin2)); // Invierte el estado del segundo LED
            tenHzPreviousMillis = currentMillis; // Actualiza el tiempo del último cambio de estado
        }
    } else { // Reinicia el ciclo
        tenHzPreviousMillis = currentMillis; // Reinicia el tiempo del último cambio de estado
    }
  }



 if (tenHzBlinking) { 
    unsigned long currentMillis = millis();
    unsigned long elapsedTime = currentMillis - tenHzPreviousMillis; // Tiempo transcurrido desde el último cambio de estado
    
    // Determinar la frecuencia de parpadeo en función del tiempo transcurrido
    int blinkFrequency;
    if (elapsedTime < 20000) { // Primer intervalo: 20 segundos parpadeando
        blinkFrequency = 10; // Frecuencia de parpadeo constante a 10 Hz
    } else { // Segundo intervalo: 20 segundos apagados
        digitalWrite(ledPin1, LOW); // Apaga el primer LED
        digitalWrite(ledPin2, LOW); // Apaga el segundo LED
        blinkFrequency = 0; // Frecuencia cero, es decir, LEDs apagados
    }

    int blinkInterval = 1000 / blinkFrequency; // Calcular el intervalo de parpadeo en milisegundos

    // Verificar si ha pasado el tiempo suficiente para cambiar de estado
    if (currentMillis - tenHzPreviousMillis >= blinkInterval) {
        digitalWrite(ledPin1, !digitalRead(ledPin1)); // Invierte el estado del primer LED
        digitalWrite(ledPin2, !digitalRead(ledPin2)); // Invierte el estado del segundo LED
        tenHzPreviousMillis = currentMillis; // Actualiza el tiempo del último cambio de estado para el parpadeo a 10 Hz
    }
    
    // Si han pasado 40 segundos (20 segundos encendidos y 20 segundos apagados), reiniciar el ciclo
    if (elapsedTime >= totalInterval) {
        tenHzPreviousMillis = currentMillis; // Reinicia el tiempo para comenzar el siguiente ciclo
    }
  }
  
  if (blinking) { // Si el parpadeo está activado
    unsigned long currentMillis = millis(); // Obtiene el tiempo actual
    unsigned long elapsedTime = currentMillis - previousMillis; // Calcula el tiempo transcurrido desde el último cambio de estado

    if (elapsedTime < 10000) { // Si han pasado menos de 5 segundos
      if ((elapsedTime % (2 * blinkInterval)) < blinkInterval) { // Si estamos en el período de encendido
        analogWrite(ledPin1, intensity * 255 / 100); // Establece la intensidad del primer LED
        analogWrite(ledPin2, intensity * 255 / 100); // Establece la intensidad del segundo LED
      } else { // Si estamos en el período de apagado
        digitalWrite(ledPin1, LOW); // Apaga el primer LED
        digitalWrite(ledPin2, LOW); // Apaga el segundo LED
      }
    } else { // Si han pasado 5 segundos
      digitalWrite(ledPin1, LOW); // Apaga el primer LED
      digitalWrite(ledPin2, LOW); // Apaga el segundo LED
      
      if (elapsedTime >= totalInterval) { // Si ha pasado el intervalo total de 2 minutos
        previousMillis = currentMillis; // Reinicia el tiempo para comenzar el siguiente ciclo
      }
    }
  }
}

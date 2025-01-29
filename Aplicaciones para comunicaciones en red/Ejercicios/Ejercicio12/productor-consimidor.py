import threading
import time

BUFFER = 5
buffer = []
buffer_condition = threading.Condition()

def productor():
    global buffer
    while True:
        item = 1  # Genera un elemento
        with buffer_condition:  # Adquiere el bloqueo antes de acceder al búfer
            while len(buffer) == BUFFER:  # Si el búfer está lleno, espera
                buffer_condition.wait()
            buffer.append(item)  # Coloca el elemento en el búfer
            print(f'Productor produce {item}. Búfer: {buffer}')
            buffer_condition.notify_all()  # Notifica a todos los hilos que están esperando
        time.sleep(1)  # Espera un tiempo

def consumidor():
    global buffer
    while True:
        with buffer_condition:  # Adquiere el bloqueo antes de acceder al búfer
            while len(buffer) == 0:  # Si el búfer está vacío, espera
                buffer_condition.wait()
            item = buffer.pop(0)  # Toma el primer elemento del búfer
            print(f'Consumidor consume {item}. Búfer: {buffer}')
            buffer_condition.notify_all()  # Notifica a todos los hilos que están esperando
        time.sleep(1)  # Espera un tiempo

producer_threads = []
consumer_threads = []
# Crea los hilos de productores
for _ in range(5):
    producer_thread = threading.Thread(target=productor)
    producer_threads.append(producer_thread)
# Crea los hilos de consumidores
for _ in range(5):
    consumer_thread = threading.Thread(target=consumidor)
    consumer_threads.append(consumer_thread)

for producer_thread in producer_threads:
    producer_thread.start()
for consumer_thread in consumer_threads:
    consumer_thread.start()

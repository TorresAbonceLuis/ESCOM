import threading
import time

BUFFER = 5

# Semáforos para controlar el acceso al búfer(restricciones)
empty = threading.Semaphore(BUFFER)
full = threading.Semaphore(0)
buffer = []
def productor():
    while True:
        item = 1  # Genera un elemento
        empty.acquire()  # Espera a que haya espacio en el búfer
        buffer.append(item)  # Coloca el elemento en el búfer
        print(f'Productor produce {item}. Búfer: {buffer}')
        full.release()  # Incrementa el contador de elementos en el búfer
        time.sleep(1)  # Espera un tiempo
def consumidor():
    while True:
        full.acquire()  # Espera a que haya al menos un elemento en el búfer
        item = buffer.pop(0)  # toma el primer elemento del búfer
        print(f'Consumidor consume {item}. Búfer: {buffer}')
        empty.release()  # Incrementa el contador de espacio disponible en el búfer
        time.sleep(1)  # Espera un tiempo
producer_threads = []
consumer_threads = []
# Crea los hilos de productores
for _ in range(5):
    producer_thread = threading.Thread(target=productor)
    producer_threads.append(producer_thread)
# Crea los hilos de consumidores
for _ in range(1):
    consumer_thread = threading.Thread(target=consumidor)
    consumer_threads.append(consumer_thread)

for producer_thread in producer_threads:
    producer_thread.start()
for consumer_thread in consumer_threads:
    consumer_thread.start()
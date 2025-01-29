from pythoned.grafos import Grafo, Vertice
from pythoned.basicas import Cola

def bea(g,inicio):
  inicio.asignarDistancia(0)
  inicio.asignarPredecesor(None)
  colaVertices = Cola()
  colaVertices.agregar(inicio)
  while (colaVertices.tamano() > 0):
    verticeActual = colaVertices.avanzar()
    for vecino in verticeActual.obtenerConexiones():
      if (vecino.obtenerColor() == 'blanco'):
        vecino.asignarColor('gris')
        vecino.asignarDistancia(verticeActual.obtenerDistancia() + 1)
        vecino.asignarPredecesor(verticeActual)
        colaVertices.agregar(vecino)
    verticeActual.asignarColor('negro')
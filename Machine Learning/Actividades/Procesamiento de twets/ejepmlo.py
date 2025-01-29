import re
import emoji

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return contenido

def obtener_emojis(texto):
    return re.findall(r'[\U0001F300-\U0001F6FF\U0001F900-\U0001F9FF\U00002600-\U000027BF\U0001f600-\U0001f64F\U0001f680-\U0001f6FF\U000025A0-\U0001F251]+', texto)

def crear_diccionario_emojis(texto):
    emojis = obtener_emojis(texto)
    diccionario_emojis = {}
    for e in emojis:
        descripcion = emoji.demojize(e).replace(':', '').replace('_', ' ')
        diccionario_emojis[e] = descripcion
    return diccionario_emojis

def reemplazar_emojis(texto, diccionario_emojis):
    for emoji, descripcion in diccionario_emojis.items():
        texto = texto.replace(emoji, descripcion)
    return texto

nombre_archivo = 'tweets_asco   .txt'
texto = leer_archivo(nombre_archivo)
diccionario_emojis = crear_diccionario_emojis(texto)
texto_con_descripciones = reemplazar_emojis(texto, diccionario_emojis)

print("Diccionario de emojis:")
print(diccionario_emojis)
print("\nTexto con descripciones de emojis:")
print(texto_con_descripciones)


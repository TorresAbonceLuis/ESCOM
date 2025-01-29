import re

def eliminar_menciones(texto):#elimina menciones punto 1
    return re.sub(r'@[\w_]+', '', texto)# expresión regular para eliminar menciones

def eliminar_enlaces(texto):#elimina enlaces URLs punto 2
    return re.sub(r'http\S+', '', texto)# expresión regular para eliminar enlaces

def limpiar_texto(texto):#elimina caracteres especiales y puntuación punto 3
    texto_limpio = re.sub(r'[^\w\s]', '', texto)# expresión regular para eliminar caracteres especiales y puntuación
    return ' '.join(texto_limpio.split())#eliminar espacios en blanco

def eliminar_stopwords(texto):#elimina stopwords punto 5
    stopwords = ['y', 'e', 'o', 'u', 'a', 'de', 'la', 'el', 'en', 'con', 'por', 'para', 'entre', 'un', 'una', 'uno', 'unas', 'unos']
    palabras = texto.split()#separar el texto en palabras
    return ' '.join([palabra for palabra in palabras if palabra.lower() not in stopwords])#eliminar las palabras que estén en la lista de stopwords

def procesar_tweet(tweet):
    tweet = tweet.lower()  # Convertir todo el texto a minúsculas punto 10
    tweet_sin_menciones = eliminar_menciones(tweet)
    tweet_sin_enlaces = eliminar_enlaces(tweet_sin_menciones)
    tweet_limpio = limpiar_texto(tweet_sin_enlaces)
    tweet_sin_stopwords = eliminar_stopwords(tweet_limpio)
    return tweet_sin_stopwords

def main():
    with open('tweets_asco.txt', 'r', encoding='utf-8') as archivo:#abrir el archivo
        tweets = archivo.readlines()#leer el archivo
    tweets_procesados = [procesar_tweet(tweet) for tweet in tweets]#procesar los tweets
    with open('tweets_asco_procesados.txt', 'w', encoding='utf-8') as archivo_procesado:#escribir los tweets procesados
        for tweet in tweets_procesados:#escribir los tweets procesados
            archivo_procesado.write(tweet + '\n')#escribir los tweets procesados

main()

# -*- coding: utf-8 -*-
"""
@author: Jose Pezantes
"""
import pandas as pd
import re      #expresiones regulares


dataset = "C:/Users/LENOVO/OneDrive/TT_ViolenciaPolíticaGénero/tweets.csv"
df = pd.read_csv(dataset)
df.columns
tweets = df.Text #obtiene el texto del tweet

#preprocesamiento  de los tweets
processed_tweets = []
#re.sub("cadena a buscar", "con la que se reemplaza", cadena_leida)
url = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
        '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
menciones = '@[\w\-]+'
hashtag = '#[\w\-]+'
#caracteres_especiales = r'\W'
caracter_individual=r'\s+[a-zA-Z]\s+'
caracter_individual_inicio= r'\^[a-zA-Z]\s+'
varios_espacios= r'\s+'
prefijo_b = r'^b\s+'
numeros = '[0-9]+'

for tweet in tweets:
    tweet_procesado = tweet.lower()  #Convertir a minúsculas
    tweet_procesado = re.sub(menciones, ' ', tweet_procesado)
    tweet_procesado = re.sub(hashtag, ' ', tweet_procesado)
    tweet_procesado = re.sub(url, ' ', tweet_procesado)
    #tweet_procesado = re.sub(caracteres_especiales, ' ', tweet_procesado)
    tweet_procesado = re.sub(caracter_individual, ' ', tweet_procesado)
    tweet_procesado = re.sub(caracter_individual_inicio, ' ', tweet_procesado) 
    tweet_procesado = re.sub(prefijo_b, '', tweet_procesado)
    tweet_procesado = re.sub(numeros, ' ', tweet_procesado)
    tweet_procesado = re.sub(" rt | amp ", ' ', tweet_procesado)
    tweet_procesado = re.sub(" q ", ' que ', tweet_procesado)
    tweet_procesado = re.sub(" sr ", ' señor ', tweet_procesado)
    tweet_procesado = re.sub(" sra ", ' señora ', tweet_procesado)
    tweet_procesado = re.sub(" ud ", ' usted ', tweet_procesado)
    tweet_procesado = re.sub(" x ", ' por ', tweet_procesado)
    tweet_procesado = re.sub(" d ", ' de ', tweet_procesado)
    tweet_procesado = re.sub(" xq ", ' porque ', tweet_procesado)
    tweet_procesado = re.sub(varios_espacios, ' ', tweet_procesado, flags=re.I)
    
    processed_tweets.append(tweet_procesado)   #agregar a la lista de tweets procesados

#crear y guardar dataset etiquetado limpio
tweets = processed_tweets
df_temp = pd.DataFrame(columns=["text"])
for tweet in tweets: df_temp.loc[len(df_temp)] = [tweet]
df_temp.to_excel("C:/Users/LENOVO/OneDrive/TT_ViolenciaPolíticaGénero/data_clean2.xlsx")
df_temp.to_csv("C:/Users/LENOVO/OneDrive/TT_ViolenciaPolíticaGénero/data_clean2.csv", sep=',', encoding="utf-8")
print(df_temp.describe())


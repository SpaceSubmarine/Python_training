import numpy as np
import pandas as pd 
from pandas import ExcelWriter
from bs4 import BeautifulSoup
import requests

#====== ESTE CODIGO CREA EL EXCEL CON LOS RESGISTROS Y CÁLCULOS EXPORTADOS DE COINGEKO =======


#   FALTA ACABAR SCRIPT DE WEB SCRAPING DE PRECIOS .....!!!!!!!!!!!!!!!!
page = requests.get('https://www.coingecko.com/es')
soup = BeautifulSoup(page.text, 'html.parser')

body_items = soup.find_all('body')

for body in body_items:
    BTC = body.find(class_="no-wrap").text
print(BTC)

#Creación del data frame:
df = pd.DataFrame({
                   'Currency': [BTC, "ETH", "ADA", "SOl"],
                   'ATH ($)': [60000, 3600, 3, "ni puta idea"],
                   'Value ($)': [40000, 3000, 1.3, 180]})
df = df[['Currency', 'ATH ($)', 'Value ($)']]

#Escritura del data frame en formato excel 
writer = ExcelWriter('practica/cripto_practica_V01.xlsx')


# index=True nos crea la columna del índice de registros
df.to_excel(writer, 'DF_1', index=True)     
writer.save()


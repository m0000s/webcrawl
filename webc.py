#!/usr/bin/python3
#Project started: 12/12/2018 20:14

import sys
from time import sleep
from bs4 import BeautifulSoup
from urllib import request

#Busca las urls
def parse_urls(query,code):
    soup = BeautifulSoup(code,'lxml') #Establece un parseo de tipo lxml sobre el codigo
    outp_uri = soup.find_all('a',class_='web-bing__title') #Parsea en el codigo buscando urls
    print(W+'\n[['+B+'[ Search '+G+query+B+' results. ]'+W+']]')
    #Lee la lista de links recaudados
    for p in range(len(outp_uri)):
        print('    ['+G+' _ '+W+']'+outp_uri[p]['href'])

R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[1;34m"
Y = "\033[1;33m"
W = "\033[1;37m"

#Si no ingresó ninguna query muestra el mensaje
usage = '%sUsage: %s%s <query search>' % (G,W,sys.argv[0])
if len(sys.argv) == 1:
   print(usage)
#Verifica si es más de 1 query
elif len(sys.argv) > 2:
   search_links = list(','*len(sys.argv))
   #Agrega las query's a las urls que se parsearán
   try:
       k = 1
       for k in range(len(sys.argv)):
           search_links[k] = 'http://www.webcrawler.com/serp?q='+sys.argv[k]
       #Hace la busqueda y ejecuta la funcion donde se parsea la url
       for o in range(len(search_links)):
           code = request.urlopen(search_links[o]).read()
           parse_urls(sys.argv[o+1],code)
           sleep(5) #Espera 1 segundo
   except IndexError:
       print(R+'Error. '+W+'Input any query.\n'+usage)
#Verifica si es 1 query (verifica 2 porque en sí
#ejecutar webc.py cuenta como 'query')
elif len(sys.argv) == 2:
   search_link = request.urlopen('http://www.webcrawler.com/serp?q='+sys.argv[1]).read()
   parse_urls(sys.argv[1],search_link)
else:
    print('Unexpected error.')

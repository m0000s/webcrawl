#!/usr/bin/python3
#Project started: 12/12/2018 20:14

import sys
from time import sleep
import re
from bs4 import BeautifulSoup
from urllib import request

#Busca las urls
def parse_urls(query,code):
    soup = BeautifulSoup(code,'lxml') #Establece un parseo de tipo lxml sobre el codigo
    outp_uri = soup.find_all('a',class_='web-bing__title') #Parsea en el codigo buscando urls
    print('[[[[[[ '+query+' ]]]]]]\n')
    #Lee la lista de links recaudados
    for p in range(len(outp_uri)):
        print(outp_uri[p]['href'])

#Si no ingreso ninguna query muestra el mensaje
if len(sys.argv) == 1:
   print('Usage: %s <query search>' % (sys.argv[0]))
#Verifica si es más de una query
elif len(sys.argv) > 2:
   search_links = []
   #Agrega las querys a las urls que se parsearán
   for k in range(len(sys.argv)):
       search_links.append('http://www.webcrawler.com/serp?q='+sys.argv[k])
   #Hace la busqueda y ejecuta la funcion donde se parsea la url
   for o in range(len(search_links)):
       code = request.urlopen(search_link[o]).read()
       parse_urls(sys.argv[k],code)
       sleep(1) #Espera 1 segundo
#Verifica si es una query
elif len(sys.argv) == 2:
   search_link = request.urlopen('http://www.webcrawler.com/serp?q='+sys.argv[1]).read()
   parse_urls(sys.argv[1],search_link)
else:
    print('Unexpected error.')

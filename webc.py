#!/usr/bin/python3
#Project started: 12/12/2018 20:14

import sys
from time import sleep
from bs4 import BeautifulSoup
from urllib import request

#
#webcrawler.com search class
class webcrawler_com:
    def parse_urls(query,code):
        soup = BeautifulSoup(code,'html.parser')
        outp_uri = soup.find_all('a',class_='web-bing__title')
        print(W+'\n[['+B+'[ Searching '+G+query+B+' results. ]'+W+']]')
        def parse_titles(uri,i):
            outp_title = soup.find_all('a',string=True)
            return outp_title[i].get_text()
        for p in range(len(outp_uri)):
            url = outp_uri[p]['href']
            title = parse_titles(url,p)
            print('    ['+G+' _ '+W+']'+url+R+' - '+W+title)
        print(G+'    [ '+W+'_'+G+' ] Succes '+W+str(p)+' results found.\n')
banner = '''
           ;               ,\n         ,;                 '.\n        ;:                   :;
       ::                     ::\n       ::                     ::\n       ':                     :
        :.                    :\n     ;' ::                   ::  '\n    .'  ';                   ;'  '.
   ::    :;                 ;:    ::\n   ;      :;.             ,;:     ::\n   :;      :;:           ,;"      ::
   ::.      ':;  ..,.;  ;:'     ,.;:\n    "'"...   '::,::::: ;:   .;.;""'\n        '"""....;:::::;,;.;"""
    .:::.....'"':::::::'",...;::::;.\n   ;:' '""'"";.,;:::::;.'""""""  '::\n  ::'         ;::;:::;::..         :;
 ::         ,;:::::::::::;:..       ::\n ;'     ,;;:;::::::::::::::;";..    ':.\n::     ;:"  ::::::"""'::::::  ":     ::
 :.    ::   ::::::;  :::::::   :     ;\n  ;    ::   :::::::  :::::::   :    ;\n   '   ::   ::::::....:::::'  ,:   '
    '  ::    :::::::::::::"   ::\n       ::     ':::::::::"'    ::\n       ':       """""""'      ::
        ::                   ;:\n        ':;                 ;:"\n          ';              ,;'
'''
R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[1;34m"
Y = "\033[1;33m"
W = "\033[1;37m"
querys = [sys.argv[1:]]

#
##Search function
def search():
    if len(querys) > 2:
       search_links = list(','*(len(querys)-1))
       syss = []
       print(banner)
       sleep(5)
       try:
           k = 1
           while k < len(querys):
               syss.append(querys[k])
               k += 1
           for o in range(len(search_links)):
               search_links[o] = 'http://www.webcrawler.com/serp?q='+syss[o]
               code = request.urlopen(search_links[o]).read()
               webcrawler_com.parse_urls(syss[o],code)
               sleep(3)
       except SyntaxError:
           print(R+'Error. '+W+'Input any query.\n'+usage)
    elif len(querys) == 2:
       search_link = request.urlopen('http://www.webcrawler.com/serp?q='+querys[1]).read()
       print(banner)
       sleep(5)
       webcrawler_com.parse_urls(querys[1],search_link)
    else:
        print('Unexpected error.')
#
##Menu function
def menu():
    def show_help():
       print(R+'\nCommand      Function\n'+W+'exit         Exit to webc.\n?            Display help.\nadd <query>  Add query to the config search.\nrun          Run the config.\n')
    commands = 'exit','run','?','add'
    print('Input \'?\' for help.')
    while True:
       try:
           e = input(W+'$'+B+'w3bc'+R+' >> '+B).split(' ')
       except KeyboardInterrupt:
           print(R+'\nExiting '+W+'Control+c pushed.')
           break
       if e[0] in commands:
          if e[0] == 'exit':
             break
          elif e[0] == '?':
             show_help()
          elif e[0] == 'run':
             try:
                 if len(querys) > 1:
                     search()
                 elif len(querys) == 1:
                     print(R+'Not '+W+'have querys. Add querys.')
             except KeyboardInterrupt:
                 print(R+'Exiting '+W+'Control+c pushed.')
                 break
          if e[0] == 'add':
             querys.append(e[1])
       elif e not in commands:
            print(R+'Error: '+W+'Command \''+e[0]+'\' not found')

#
#Conditional area
if len(sys.argv) == 1:
    menu()
elif len(sys.argv) > 1:
    if '-r' in sys.argv[1:]:
        search()
    elif '-h' in sys.argv[1:]:
        menu(show_help())
    else:
        print(G)
        print('Usage:%s %s%s -h  %s           To help.\n   %sOr:%s%s %s <query(s)> -r  %sTo run te search.\n   %sOr:%s%s %s  %s              To explained version. ' % (W,B,sys.argv[0],W,G,W,B,sys.argv[0],W,G,W,B,sys.argv[0],W))

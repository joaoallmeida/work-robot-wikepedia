import pandas as pd 
import urllib.request
import os
import getpass
from text import theme

usr = getpass.getuser()

FILENAME  = 'url.json' # definindo qual arquivo deve ser lido. 
FILE_PATH = 'C:/Users/' + usr + '/Desktop/' + theme + '/' # definindo caminho para pasta 

os.mkdir(FILE_PATH) # criando a pasta no desktop

urls = pd.read_json(FILENAME) # lendo o arquivo .json com pandas.

def get_url(i, url,file_path):  
    filename = 'image-{}.jpg'.format(i)       
    full_path = '{}{}'.format(file_path,filename)
    urllib.request.urlretrieve(url,full_path)


    print ('{} saved in your desktop.'.format(filename))

    return None

#função principal, com um for para percorrer o arquivo .json e traz seus valores. 
def main_image():    
    for i,url in enumerate(urls.values):
        get_url(i, url[0],FILE_PATH) # url[0], significa começar a percorrer os valores do arquivo 
                                        # pelo ponto/(indice) zero. 
    quit() 
main_image()






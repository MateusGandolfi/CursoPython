import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLerror:
    print (f'\033[31mNao e possivel acessar o site Pudim!\033[m')
else:
    print (f'\033[32mO site Pudim esta acessivel.\033[m')

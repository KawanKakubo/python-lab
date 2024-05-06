import urllib
import urllib.request


try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('O site do Youtube não está acessível no momento.')
else:
    print('Consegui acessar o site do Youtube com sucesso.')

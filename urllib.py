import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.spotify.com')
    print('O site esta disponível')

except:
    print('O site nao está disponível')
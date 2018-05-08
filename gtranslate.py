import requests
import re
from socket import *


def translate(message):
    url = 'https://translate.google.com/?hl=ja#en/ja/'
    r = requests.get(url, params={'q': message})
    pattern = "TRANSLATED_TEXT=\'(.*?)\'"
    result = re.search(pattern, r.text).group(1)
    return result

def make_socket():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    serverSocket.bind(("localhost",6000))
    serverSocket.listen(1)
    tcpCliSock,addr = serverSocket.accept()
    message=tcpCliSock.recv(1024)
    print(message)
    #message_after=translate(message.encode('utf-8'))
    tcpCliSock.send(message)
    tcpCliSock.close()

if __name__ == '__main__':
    make_socket()

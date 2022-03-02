#!/usr/bin/python3

# - *- coding: utf- 8 - *-

"""
Aplicação: ScanPortTest
Função: Faz uma varredura em um determinado host
        a procura a procura de portas abertas.
Desenvolvedor: Werdeles Marcio de C. Soares
Versão: 1.0.3
---------------------------------------------------
Contato: werdelesmarcio@gmail.com 
"""

import socket
import sys
from colorama import Fore
from colorama import Back
from colorama import Style # para utilizar cores no texto (requer instalar colorama via pip: pip install colorama)

if len(sys.argv) != 4:
    print("[!] Usar: scan.py [target] [initial_port] [final_port]")
    sys.exit(1)

def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    try:
        s.connect((host, port))
        return(1)
    except:
        return(2)

host = str(sys.argv[1])
initport = int(sys.argv[2])
finalport = int(sys.argv[3])

print("\n--------- Iniciando Escaneamento ----------\n")
print("[*] Conectando ao %s\n[*] Escaneando o range de portas de %s para %s ..." % (host, initport, finalport))
print()

for port in range(initport, finalport+1):
    e = connect(host, port)
    if e != 2:
        print(Fore.WHITE + Style.BRIGHT + Back.CYAN + "[+] Porta: %s - Status: OPEN." % port + Style.RESET_ALL)

print("\n--------- Escaneamento Concluido ----------\n")

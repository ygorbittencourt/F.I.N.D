# F.I.N.D - F(for).I(intern).N(network).D(discovery)
# Autor: Ygor Bittencourt
# Versão: 1.3 
# 2016-2021
# MIT for you! :) 
#
#   F.I.N.D foi desenvolvido para fazer descoberta silenciosa a partir de um seguimento de rede interna.
#
#   Dificilmente um firewall bloqueia pacotes ARP(Isso é bastante incomum, realmente incomum!!).
#   Devemos ainda levar em consideração que o windows firewall por padrão também não bloqueia pacotes ARP.
#
#   É dessa forma que o F.I.N.D consegue localizar máquinas ativas sem levantar suspeitas, mesmo que o firewall delas esteja ativado.
#   Encontrar os HOSTS UP é quase certo, já as portas não tem jeito, se existir um firewall bloqueando-as elas não serão listadas.
#
#   Originalmente você pode alterar as portas do SCAN na linha 27! Mas lembre-se que a vantagem é ser silencioso.
#
#         =======> É necessário instalar a LIB Scapy, no terminal digite: sudo pip install scapy <=======
#                    FOR USAGE: sudo python3 %s 192.168.1.1(ou uma rede completa 192.168.1.1/24)
#   
#   Enjoy

import sys
import argparse
from scapy.all import *

arguments = len(sys.argv)
if arguments == 1:
    print (" Opa!! Faltaram parâmetros, use:  sudo python3 %s 192.168.1.1(ou uma rede completa 192.168.1.1/24)" % (sys.argv[0]))

if arguments > 1:
    ports = [22,80,443,3389]  ## <=============  Você pode alterar a quantidade de portas aqui.

    ##### Fun Part!
    print('\n\n==============================================================================')
    print('============= F.I.N.D - F(for).I(intern).N(network).D(discovery) =============')
    print('==============================================================================')
    print('\n F.I.N.D processando, aguarde... (principalmente se você colocou uma rede \n inteira /24 ou alterou a quantidade de portas!)\n\n')

    ListaARP = []

    def FIND(input_addr):
        CorpoDaRequisicao = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=input_addr)
        ans, unans = srp(CorpoDaRequisicao, timeout=3, retry=2)
        
        for sent, received in ans:
            ListaARP.append({'1': received.psrc, '2': received.hwsrc})

        return ListaARP


    def inicio():
        recon = []
        Scan = FIND(sys.argv[1])
        for ObjMapa in Scan:

            try:
                syn = IP(dst=ObjMapa['1']) / TCP(dport=ports, flags="S")
            except socket.gaierror:
                raise ValueError('Problema ao resolver o host {}. Verifique sua configuração de DNS(provavelmente).'.format(ip))

            ans, unans = sr(syn, timeout=2, retry=1)
            
            for sent, received in ans:
                if received[TCP].flags == "SA":
                    recon.append({'1': ObjMapa['1'], '2':received[TCP].sport})

        print('\n\n=================================================')
        print('============= Resultados do F.I.N.D =============')
        print('=================================================')
        
        print('\n==> Hosts UP vs MACs Coletados ==================\n')
        for ObjMapa in Scan:
            print('    HOST: {} ==> MAC: {}'.format(ObjMapa['1'], ObjMapa['2']))

        print('\n==> Hosts UP vs Portas Abertas ==================\n')
        for ObjMapa in recon:
            print('    HOST: {} ==> PORTA: {}'.format(ObjMapa['1'], ObjMapa['2']))
        
        print('\n==================== F.I.N.D ====================')

    if __name__ == '__main__':
        inicio()
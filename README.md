# F.I.N.D
#F.I.N.D - F(for).I(intern).N(network).D(discovery)  - A stealth Scan, network discovery using ARP packets

     F.I.N.D foi desenvolvido para fazer descoberta silenciosa a partir de um seguimento de rede interna.

   Dificilmente um firewall bloqueia pacotes ARP(Isso é bastante incomum, realmente incomum!!).
   Devemos ainda levar em consideração que o windows firewall por padrão também não bloqueia pacotes ARP.

   É dessa forma que o F.I.N.D consegue localizar máquinas ativas sem levantar suspeitas, mesmo que o firewall delas esteja ativado.
   Encontrar os HOSTS UP é quase certo, já as portas não tem jeito, se existir um firewall bloqueando-as elas não serão listadas.

   Originalmente você pode alterar as portas do SCAN na linha 27! Mas lembre-se que a vantagem é ser silencioso.

         =======> É necessário instalar a LIB Scapy, no terminal digite: sudo pip install scapy <=======
                    FOR USAGE: sudo python3 %s 192.168.1.1(ou uma rede completa 192.168.1.1/24)
   
Enjoy

# F.I.N.D
#F.I.N.D - F(for).I(intern).N(network).D(discovery)  - A stealth Scan, network discovery using ARP packets

     F.I.N.D foi desenvolvido para fazer descoberta silenciosa a partir de um seguimento de rede interna.

   Dificilmente um firewall bloqueia pacotes ARP(Isso é bastante incomum, realmente incomum!!).
   Devemos ainda levar em consideração que o windows firewall por padrão também não bloqueia pacotes ARP.

   É dessa forma que o F.I.N.D consegue localizar máquinas ativas sem levantar suspeitas, mesmo que o firewall delas esteja ativado.
   Encontrar os HOSTS UP é quase certo, já as portas não tem jeito, se existir um firewall bloqueando-as elas não serão listadas.

   Originalmente(No códdigo desse repositório) você pode alterar as portas do SCAN na linha 27! Mas lembre-se que a vantagem é ser silencioso.

         =======> Para Instalar <=======
         Clone o repositório ==> git clone https://github.com/ygorbittencourt/F.I.N.D.git
         
         =======> É necessário instalar a LIB Scapy <=======
         No terminal digite: sudo pip install scapy
         
         FOR USAGE: sudo python3 f.i.n.d.py 192.168.1.1(ou uma rede completa 192.168.1.1/24)
   
Enjoy

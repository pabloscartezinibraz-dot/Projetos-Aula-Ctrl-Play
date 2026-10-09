# Eu quero criar um cardápio de fastfood que você possa selecionar seus itens para comer, e depois de comprar, gerar uma nota
#Dícionario de Itens do Cardápio
prato_principal = {"(1) Cheeseburguer": 1, "(2) X-Bacon": 2, "(3) X-Salada": 3, "(4) Smash Burguer": 4}
acompanhamentos = {"(5) Batata-Frita": 5, "(6) Chicken Nuggets": 6, "(7) Molhos": 7, "(8) Danone": 8}
bebidas = {"(9) Suco de Laranja": 9, "(10) Suco de Morango":10, "(11) Suco de Uva":11, "(12) Suco de Maracujá":12, 
           "(13) Suco de Abacaxi com Hortelã":13, "(14) Suco de Limão":14}
sobremesas = {"(15) Casquinha de Sorvete":15, "(16) Sundae":16, "(17) Petit-gateau":17, "(18) Torta Holandesa":18}

print("Esses são os pratos principais: \n")
for pratos in prato_principal:
    print(pratos)

print("\n\n Esses são os acompanhamentos: \n")
for acomp in acompanhamentos:
    print(acomp)

print("\n\n Esses são as bebidas: \n")
for beb in bebidas:
    print(beb)

print("\n\n Esses são as sobremesas: \n")
for sobremesa in sobremesas:
    print(sobremesa)

# Pedidos

listaPedido = []

pedido = (input("Qual será o seu pedido"))
listaPedido.append(pedido)
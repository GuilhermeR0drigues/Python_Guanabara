#listas são mutaveis 
# lista[] 

# lanche.append('') *adiciona no final
# lanche.insert(0,'') adiciona aonde vc desejar

# del lanche[3] deleta
# lanche.pop(3) remove tbm
# lanche.remove('') remove o valor não o indexe

# ___.sort() deixa em ordem crescente
# ___.sort(reverse=True) deixa em orden decrescente 
# len(___) tamanho da lista

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei {v}')
print('Cheguei no final da lista')

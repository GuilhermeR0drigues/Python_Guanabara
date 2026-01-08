#fatiamento
sccp = 'Sport Clube Corinthians Paulista' 
print(sccp[:5])   #Sport
print(sccp[6:10]) #Clube
print(sccp[11:22])#Corinthians
print(sccp[23:])  #Paulista
#O ':' serve para não ter limite,ou seja, do começo ao ":N" ou até o final "N:" 
#Caso tenha [1:15:2]- esse 2 do final faz pular de 2 em 2


#analise
print(len(sccp)) #31, serve pra ver o tamanho

print(sccp.count('s',0,23)) #Quantas vezes tem oq está entre aspas

print(sccp.find('thi'))  #aonde ta oq ta entre aspas

print(sccp.rfind('thi'))  #aonde ta oq ta entre aspas começando pelo final

print('Clube' in sccp) #retorna true ou false

print(sccp.replace('Sport Clube Corinthians Paulista','SCCP'))  #troca as palavras

print(sccp.upper()) #deixa em maiusculo

print(sccp.lower()) #deixa em minusculo

print(sccp.capitalize()) #Pega td a string e deixa em minusculo, mas o campo [0] fica em maiusculo

print(sccp.title()) #deixa tdas as letra de inicio de palavra maiusculas 

print(sccp.strip()) #remove tds os espaços inuteis

print(sccp.rstrip()) #remove os espaços só pela direita

print(sccp.lstrip()) #remve os espaços só da esquerda


#DIVISÃO

print(sccp.split()) #pega uma string divide de acordo com o espaço e cria um index pra cada

#JUNÇÃO
print('-'.join(sccp)) #faz ao contrário do split (na aspas vai ser oq vai aparecer)

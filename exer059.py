n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
    elif opção == 2:
        produto = n1 * n2
        print(f'O produto entre {n1} e {n2} é {produto}.')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número entre {n1} e {n2} é {maior}.')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opção == 5:
        print('Finalizando o programa...')
    else:
        print('Opção inválida! Tente novamente.')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')
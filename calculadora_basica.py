#fazendo uma calculadora básica

#uma função pra cada operação primeiro
def adicao(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def divisao(n1,n2):
    return n1/n2

def multiplicacao(n1,n2):
    return n1*n2

#pedindo ao usuário que ele escolha uma operação
print("\nEscolha uma operação: \n[1] - Soma\n[2] - Substração\n[3] - Multiplicação\n[4] - Divisão\n")
opcao = int(input("-> "))

#pedindo ao usuário os números que ele deseja realizar a operação
n1 = float(input("\nDigite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

#realizando as operações e mostrando na tela
if opcao == 1:
    print(f"\n{n1} + {n2} = ", adicao(n1,n2))
elif opcao == 2:
    print(f"\n{n1} - {n2} = ", subtracao(n1,n2))
elif opcao == 3:
    print(f"\n{n1} x {n2} = ", multiplicacao(n1,n2))
elif opcao == 4:
    print(f"\n{n1} / {n2} = ", divisao(n1,n2))
else:
    print("Opção Inválida, Tente Novamente!")

input("\nAperte Enter para Finalizar o programa!!!\n")
print("\n -- Programa Finalizado -- \n")
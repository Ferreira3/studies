#Exercício Python 89:
#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = []
dados = []

while True:
    dados.append(str(input("Nome do aluno: ")).capitalize().strip())
    dados.append(float(input("Primeira nota: ")))
    dados.append(float(input("Segunda nota: ")))
    dados.append((dados[1] + dados[2]) / 2)
    lista.append(dados[:])
    dados.clear()


    continuar = input("Deseja continuar?[S/N] ").strip().lower()[0]
    if "n" in continuar:
        break

print("-" * 30)
print(f"No.       NOME           MÉDIA")
print("-" * 30)
for index, pessoa in enumerate(lista):
    print(f"{index}{pessoa[0]}{pessoa[3]}")

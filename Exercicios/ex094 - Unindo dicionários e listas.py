from time import sleep
pessoas = {}
pessoas1 = []
idade = 0
cont = 0
nome = ''
while True:
    pessoas["nome"] = str(input("Nome: "))
    pessoas["Idade"] = int(input("Idade: "))
    pessoas["sexo"] = str(input("Sexo [F/M]: "))
    if pessoas["sexo"] == 'f':
        nome = pessoas["nome"]
    resp = str(input("quer continuar? "))
    cont+=1
    pessoas1.append(pessoas.copy())
    idade = (idade + pessoas["Idade"])
    if resp == 'n':
        break
    while resp != 's' or resp != 'n' in resp:
        resp = str(input("Erro... Quer continuar [S/N]: "))
media = idade / cont
print('-'*30)
print(f'A) Ao todo temos {cont} pessoas cadastradas. ')
print(f'B) A média de anos é de {media}.')
print(f'C) As mulheres cadastradas foram:', end=' ')
for c in pessoas1:
    if c["sexo"] == 'f':
        print(f'{c["nome"]};')
print('Lista de pessoas acima da média:')
for i, p in enumerate(pessoas1):
    if pessoas1[i]['Idade'] >= media:
        print(f'    Nome: {p["nome"]} Sexo: {p["sexo"]}; Idade: {p["Idade"]}; ')
print('-'*30)
sleep(1.5)
print("Encerrando...")


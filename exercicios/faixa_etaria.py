idade = int(input('Digite sua idade: '))
if 0 <= idade <= 12:
    print('Você é uma criança')
elif 13 <= idade <= 18:
    print('Você é um adolescente')
elif 19 <= idade:
    print('Você é um adulto')
else:
    print('Digite uma idade válida')
    
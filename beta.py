print("Olá, hoje vamos pegar algumas informações sobre você para nosso banco de dados")

resposta = input(" Você permite nossa analise de perfil? (sim/não) ")
if resposta == "sim":
    print("certo, vamos começar ")
    nome = input("Qual é seu nome? ")
    idade = input("Certo " + nome + ", qual é sua idade? ")
    cidade = input("você nasceu em qual cidade? ")
    print("tudo certo, com base nessas informações já sei algumas coisas sobre você. ")
    input()
    nascimento = 2026 - int(idade)
    print("Bem " + nome + ",você nasceu em " + cidade + " no ano de " + str(nascimento) + " e hoje tem " + idade + " anos.")
else:
    print("tudo bem, é sua escolha. Fique bem! ")



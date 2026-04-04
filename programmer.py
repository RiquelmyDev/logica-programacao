print("bem vindo ao sistema educacional municipal. vamos avaliar seu desempenho no semestre.")
print("---------------------------------------------------------")
nome = input("Qual é seu nome? ")
nota = input("Tudo bem " + nome + ", Qual foi sua nota esse semestre?") 


if int(nota) >= 7:
    print ("Parabens " + nome + " você foi aprovado com uma nota referente a " + nota + " pontos. ")
elif int(nota) < 5:
    print("Você está reprovado.")
else:
    print ("você esta de recuperação. ")
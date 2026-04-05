alunos = [1, 2 , 3, 4 , 5]
alunos.insert(1, [24.1, 25, 20, 21])
alunos.insert(2, [10, 20, 18, 21])
alunos.insert(3, [17, 23, 17, 23])
alunos.insert(4, [14, 19, 10, 25])
alunos.insert(5, [15, 22, 15, 25])
print (alunos[2])

media = 0

for nota in alunos[1]:
    media += nota

media /= 4

print(f" o print da media do aluno 1 é: {media} ")
# analisador_notas.py

"""estou criando uma função para ler todas notas, somalas e depois pegar minha soma,
 e dividir pela quantidade de notas para ver minha media. depois depois eu retorno a media"""
def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media


""" aqui eu pego a media do aluno e classificado em qual classe ele se encaixa de acordo com a sua media"""
def classificar_aluno(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


"""Aqui eu faço uma função que nessa mesma tem lista chamada resultados, 
nessa lista eu pego cada aluno e sua nota respetiva em alunos, 
e exibo uma lista classsificando seu nome, sua nota a sua media e se ele foi aprovado ou reprovado. pego essa lista, 
guardo ela na lista resultados depois retorno ela para exibir para o usuario"""
def processar_alunos(alunos):
    resultados = []
    for aluno in alunos:
        nome = aluno["nome"]
        notas = aluno["notas"]
        media = calcular_media(notas)
        classificacao = classificar_aluno(media)

        resultado = {
            "nome": nome,
            "notas": notas,
            "media": media,
            "classificacao": classificacao
        }

        resultados.append(resultado)

    return resultados


"""aqui eu pego essa lista resultados, e faço uma função para exibir ela parra o usuario com a lista dos alunos.
eu passo que resultados, esta pegando as informções de processar_alunos e pegando alunos como paraemtro para exibir"""
def imprimir_resultados(resultados):
    for resultado in resultados:
        print(f"{resultado['nome']}: Média = {resultado['media']:.2f}, Situação = {resultado['classificacao']}")

def main():
    alunos = [
        {"nome": "Alice", "notas": [8.5, 7.0, 9.0]},
        {"nome": "Bruno", "notas": [5.0, 6.0, 5.5]},
        {"nome": "Carla", "notas": [3.0, 4.5, 2.5]},
        {"nome": "Daniel", "notas": [10.0, 9.5, 9.0]}
    ]

    resultados = processar_alunos(alunos)
    imprimir_resultados(resultados)


"""SE O ARQUIVO FOR EXECUTADO DIRRETAMENTE, ELE SE TORNA O PRINCIPAL E RODACOMEÇA A RODAR PELA FUNÇÃO MAIN"""
if __name__ == "__main__":
    main()
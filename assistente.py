print("Boa tarde, como você está? Vamos conversar? ")

comando = input("....")

match comando:
    case "oi" | "ola" | "eai" | "hey" | "opa" | "ou":
        print("oiii, tudo bem com você?")

    case "tudo bem?" | "como você está?" | "tem passado bem?":
        resposta = input("tudo bem graças a Deus, e você como vai?")
        if resposta == "bem":
            print("Que bom que está tudo bem com você!")
        else:
            print("Oque está acontecendo? ")
    case "Você é a alexa?" | "Você é o gpt?" | "Você é o gemini?":
        print("Não cara, não sou eu KKKKKK")
    
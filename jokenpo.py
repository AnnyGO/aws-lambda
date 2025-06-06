import random

def lambda_handler(event, context):
    jogador = event.get("jogada", "").lower()
    opcoes = ["pedra", "papel", "tesoura"]

    if jogador not in opcoes:
        return {
            "statusCode": 400,
            "body": "Jogada inválida! Escolha entre: pedra, papel ou tesoura."
        }

    computador = random.choice(opcoes)

    regras = {
        "pedra": "tesoura",
        "tesoura": "papel",
        "papel": "pedra"
    }

    if jogador == computador:
        resultado = "Empate!"
    elif regras[jogador] == computador:
        resultado = "Você venceu!"
    else:
        resultado = "Computador venceu!"

    return {
        "statusCode": 200,
        "body": {
            "jogador": jogador,
            "computador": computador,
            "resultado": resultado
        }
    }

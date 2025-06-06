from jokenpo import lambda_handler

event = {
    "jogada": "pedra"  
}
context = None  

resposta = lambda_handler(event, context)

# Exibe o resultado
print(resposta)

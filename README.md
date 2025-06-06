# Função Lambda - Jokenpô

## Descrição da Função
Esta função Lambda implementa o jogo Jokenpô (Pedra, Papel ou Tesoura). O usuário envia uma jogada e a função responde com a jogada do computador e o resultado da partida.

## Teste no POSTMAN ou INSOMNIA

1. Link para teste da função no POSTMAN ou INSOMNIA: https://ryu5fybibtp2a4c2ykjo45iplm0zdicr.lambda-url.us-east-2.on.aws/
2. Crie uma nova requisição POST utilizando este link
3. Utilize este body, como exemplo de corpo da requisção:
```
{
  "jogada": "pedra"
}
```

### Para Teste Local

1. Clone ou baixe os arquivos jokenpo.py e teste.py.
2. No teste.py, você deve enviar um evento como esse, contendo uma jogada válida:
```
event = {
    "jogada": "pedra"  
}
```
Você pode mudar a jogada para "papel" ou "tesoura.

3. Com a jogada definida, execute o teste com:
```
python teste.py
```

### Entradas e Saídas:

1. Caso você insira uma jogada válida, você deverá ver uma saída semelhante a essa: 
```
{
  'statusCode': 200,
  'body': {
    'jogador': 'pedra',
    'computador': 'tesoura',
    'resultado': 'Você venceu!'
  }
}
```

2. Caso a jogada seja inválida, você verá:
```
{
  "statusCode": 400,
  "body": "Jogada inválida! Escolha entre: pedra, papel ou tesoura."
}

```
### E o mais importante de tudo...

- Divirta-se ^^
- Feito por Ana Carolina S2

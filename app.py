import requests

url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
 
response = requests.get(url)

response.status_code == 200
informacoes = response.json()
print(f'O valor do dollar em reais é: {informacoes['USDBRL']['bid']}')


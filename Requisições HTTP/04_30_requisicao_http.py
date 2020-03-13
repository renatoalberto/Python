"""
Requisições http

http é o principal protocolo de transferência usado pela internet.

instalação: pip install requests
"""
import requests

# Mesma requisição feita por um navegador quando solicitado a página do Google --------------------
req = requests.get('https://www.google.com')

# Status comuns de uma requisição (req.status_code) -----------------------------------------------
# 200 - Ok, requisição bem sucedida
# 403 - Forbidden, informação protegida por senha
# 404 - Not Found, página não encontrada
print(req.status_code)

# Cabeçalho da requisição (req.headers) -----------------------------------------------------------
print(req.headers)
print(req.headers['Date'])
print(req.headers['Content-Type'])

# A resposta dessa requisição (req.text) ----------------------------------------------------------
print(req.text)







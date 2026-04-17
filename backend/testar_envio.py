import requests
import json


URL = "http://localhost:8080/message/sendText/ZapAgendaBot"
API_KEY = "ZapAgendaSuperSecretKey"

 

numero_destino = "5585997665786" 

payload = {
    "number": numero_destino, # Enviamos apenas os números agora
    "options": {
        "delay": 1200,
        "presence": "composing",
        "linkPreview": False
    },
    "textMessage": {
        "text": "Fala Ivo! O ZapAgendaBot está oficialmente VIVO! 🚀🤖"
    }
}

headers = {
    "apikey": API_KEY,
    "Content-Type": "application/json"
}

print(f"Enviando mensagem para {numero_destino}...")

try:
    
    response = requests.post(URL, json=payload, headers=headers)
    
    if response.status_code in [200, 201]:
        print("✅ Mensagem enviada com sucesso!")
        print("Resposta:", response.json())
    else:
        print(f"❌ Erro ao enviar: {response.status_code}")
        # Se der erro, vamos ver o que a API diz para ajustar o número
        print("Detalhes:", response.text)
        
except Exception as e:
    print(f"Erro na requisição: {e}")
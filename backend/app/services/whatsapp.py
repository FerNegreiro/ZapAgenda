import requests
import json

# Configurações fixas por enquanto (depois jogamos no .env)
URL_BASE = "http://localhost:8080/message/sendText/ZapAgendaBot"
API_KEY = "ZapAgendaSuperSecretKey"

def enviar_mensagem_texto(telefone: str, mensagem: str):
    """
    Função para disparar mensagens via Evolution API.
    O número deve vir no formato '558599999999'
    """
    payload = {
        "number": telefone,
        "options": {
            "delay": 1200,
            "presence": "composing",
            "linkPreview": False
        },
        "textMessage": {
            "text": mensagem
        }
    }

    headers = {
        "apikey": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(URL_BASE, json=payload, headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
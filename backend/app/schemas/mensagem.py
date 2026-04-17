from pydantic import BaseModel
from datetime import datetime

class MensagemRequest(BaseModel):
    telefone: str
    mensagem: str
    data_agendamento: datetime 
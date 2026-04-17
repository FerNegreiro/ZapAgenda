from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.db.database import Base
from datetime import datetime

class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_nome = Column(String)
    telefone = Column(String)
    data_horario = Column(DateTime)
    mensagem_enviada = Column(Boolean, default=False)
    criado_em = Column(DateTime, default=datetime.utcnow)
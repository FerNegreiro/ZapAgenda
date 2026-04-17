from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .services.whatsapp import enviar_mensagem_texto
from .schemas.mensagem import MensagemRequest
from .db.database import engine, Base, get_db  
from .models import agendamento  

# Cria as tabelas automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ZapAgenda API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "API ZapAgenda Online!"}

@app.post("/agendar")
def criar_agendamento(request: MensagemRequest, db: Session = Depends(get_db)):
    novo_agendamento = agendamento.Agendamento(
        cliente_nome="Fernando Ivo",
        telefone=request.telefone,
        data_horario=request.data_agendamento, 
        mensagem_enviada=False
    )
    
    db.add(novo_agendamento)
    db.commit()
    db.refresh(novo_agendamento)
    
    return {"status": "Agendado para " + str(novo_agendamento.data_horario)}
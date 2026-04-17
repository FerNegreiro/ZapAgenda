from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.domain import Client, User
from app.schemas.client import ClientCreate, ClientResponse

# Substitua pelos caminhos reais da sua estrutura
# from app.db.session import get_db
# from app.models.domain import Client, User
# from app.schemas.client import ClientCreate, ClientResponse

router = APIRouter()

@router.post("/", response_model=ClientResponse, status_code=201)
def create_client(client_in: ClientCreate, db: Session = Depends(get_db)):
    """ Cadastra um novo cliente/paciente """
    
    # HACK DO MVP: Garante que o profissional existe para não dar erro de Foreign Key
    user = db.query(User).filter(User.id == client_in.professional_id).first()
    if not user:
        user = User(id=client_in.professional_id, name="Psicólogo Teste", email="teste@zapagenda.com")
        db.add(user)
        db.commit()
        db.refresh(user)

    new_client = Client(
        name=client_in.name,
        phone=client_in.phone, # Idealmente, enviar no formato: 5511999999999
        professional_id=user.id
    )
    
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    
    return new_client

@router.get("/", response_model=list[ClientResponse])
def list_clients(db: Session = Depends(get_db)):
    """ Lista todos os clientes cadastrados """
    return db.query(Client).all()
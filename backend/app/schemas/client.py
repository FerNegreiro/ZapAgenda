from pydantic import BaseModel

class ClientCreate(BaseModel):
    name: str
    phone: str
    professional_id: int = 1 # Deixamos 1 como padrão para o MVP não quebrar

class ClientResponse(BaseModel):
    id: int
    name: str
    phone: str
    professional_id: int

    class Config:
        from_attributes = True
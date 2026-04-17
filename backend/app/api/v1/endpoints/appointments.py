from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.db.database import get_db
from app.models.domain import Appointment, Client
from app.schemas.appointment import AppointmentCreate, AppointmentResponse

# ESSA É A LINHA QUE TINHA SUMIDO:
router = APIRouter()

@router.post("/", response_model=AppointmentResponse, status_code=201)
def create_appointment(appointment_in: AppointmentCreate, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == appointment_in.client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    new_appointment = Appointment(
        client_id=appointment_in.client_id, 
        scheduled_at=appointment_in.scheduled_at
    )
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment

@router.get("/upcoming", response_model=list[AppointmentResponse])
def get_upcoming_appointments(db: Session = Depends(get_db)):
    # Janela de 12h atrás até 36h no futuro (evita erro de fuso horário)
    start = datetime.utcnow() - timedelta(hours=12)
    end = datetime.utcnow() + timedelta(hours=36)
    
    # Buscamos TODOS (removido o filtro de reminder_sent=False)
    upcoming = db.query(Appointment).join(Client).filter(
        Appointment.scheduled_at >= start,
        Appointment.scheduled_at <= end
    ).all()

    for appt in upcoming:
        appt.client_name = appt.client.name if appt.client else "Cliente"
    
    return upcoming
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AppointmentBase(BaseModel):
    client_id: int
    scheduled_at: datetime
    notes: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentResponse(AppointmentBase):
    id: int
    reminder_sent: bool
    client_name: Optional[str] = None # <-- ESTA LINHA É O SEGREDO

    class Config:
        from_attributes = True
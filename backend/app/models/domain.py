from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    """O Profissional (Ex: Psicólogo)"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    plan = Column(String, default="gratis") # gratis, pago_29, pago_49
    
    clients = relationship("Client", back_populates="professional")

class Client(Base):
    """O Cliente final (Ex: Paciente)"""
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True, index=True)
    professional_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False) # Número do WhatsApp
    
    professional = relationship("User", back_populates="clients")
    appointments = relationship("Appointment", back_populates="client")

class Appointment(Base):
    """O Agendamento"""
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    scheduled_at = Column(DateTime, nullable=False)
    reminder_sent = Column(Boolean, default=False)
    
    client = relationship("Client", back_populates="appointments")
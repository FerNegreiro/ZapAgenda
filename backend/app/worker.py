import time
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.agendamento import Agendamento
from app.services.whatsapp import enviar_mensagem_texto
from datetime import datetime

def monitorar_e_enviar():
    print("🚀 Vigilante Inteligente iniciado...")
    while True:
        db = SessionLocal()
        try:
            agora = datetime.now()
            # BUSCA APENAS: não enviado E que o horário já passou ou é agora
            pendentes = db.query(Agendamento).filter(
                Agendamento.mensagem_enviada == False,
                Agendamento.data_horario <= agora
            ).all()

            for agenda in pendentes:
                print(f"🔔 Enviando lembrete para {agenda.telefone}...")
                
                
                msg = f"Olá! Este é um lembrete do ZapAgenda para {agenda.cliente_nome}."
                
                res = enviar_mensagem_texto(agenda.telefone, msg)
                
                if "key" in res: 
                    agenda.mensagem_enviada = True
                    db.commit()
                    print(f"✅ Mensagem enviada e banco atualizado!")
                else:
                    print(f"❌ Erro ao enviar para {agenda.telefone}")

        except Exception as e:
            print(f"Erro no loop do worker: {e}")
        finally:
            db.close()
        
        
        time.sleep(60)

if __name__ == "__main__":
    monitorar_e_enviar()
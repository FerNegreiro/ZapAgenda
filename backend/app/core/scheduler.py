from apscheduler.schedulers.background import BackgroundScheduler
from app.db.database import SessionLocal
from app.services.whatsapp import send_reminders

def job():
    db = SessionLocal()
    try:
        send_reminders(db) # Chama a função que envia e marca como True
    finally:
        db.close()

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", minutes=1)
    scheduler.start()
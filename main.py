from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware # NOWA LINIJKA
from pydantic import BaseModel
from sqlalchemy.orm import Session
import database

app = FastAPI(title="SIEM Log API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LogCreate(BaseModel):
    source_ip: str
    severity: str
    event_type: str
    message: str

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/logs/", status_code=201)
def create_log(log: LogCreate, db: Session = Depends(get_db)):
    db_log = database.LogEvent(
        source_ip=log.source_ip,
        severity=log.severity,
        event_type=log.event_type,
        message=log.message
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return {"message": "Log zapisany pomyślnie!", "log_id": db_log.id}

@app.get("/logs/")
def read_logs(db: Session = Depends(get_db)):
    logs = db.query(database.LogEvent).order_by(database.LogEvent.id.desc()).limit(100).all()
    return logs
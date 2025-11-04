from fastapi import FastAPI,Depends,HTTPException
import database
app = FastAPI()
import schemas
from sqlalchemy.orm import Session
from sqlalchemy import func
import models

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home(name :str="guest"):
    return {"message":f"welcome to home '{name}'"}

@app.post('/contacts')
def create_contacts(contact:schemas.ContactForm,db:Session=Depends(get_db)):
    new_contact = models.Contacts(name=contact.name,email=contact.email,message=contact.message)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return {"message":"contact added succesfully"}
    


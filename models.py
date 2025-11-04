from sqlalchemy import Column,Integer,String,ForeignKey,Float
from sqlalchemy.orm import relationship
from database import Base

class Contacts(Base):
    __tablename__="contacts"
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    message = Column(String)
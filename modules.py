import sqlite3
import sqlalchemy
from sqlalchemy import (create_engine,
                        Column,
                        Integer,
                        String,
                        Float,
                        DateTime
                        )


from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine('sqlite:///project.db')
Base = declarative_base()



class Password(Base):

    __tablename__ = "Passwords"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    pssw = Column("Password", String)
    date = Column("Date", DateTime, default=datetime.datetime.now)

    def __init__(self, name, pssw):
        self.name = name
        self.pssw = pssw


    def __repr__(self):
        return f"{self.id} {self.name} {self.pssw} {self.date}"



Base.metadata.create_all(engine)







# import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy import Column, Integer, String, Float, DateTime
# from sqlalchemy.ext.declarative import declarative_base
#
# class Password(Base):
#     __tablename__ ="Passwords"
#     id = Column(Integer, primary_key=True)
#     name = Column("Name", String)
#     pssw = Column("Password", String)
#     date = Column("Date", DateTime, default=datetime.datetime.utcnow)
#
#
#     def __init__(self, name):
#         self.name = name
#
#     def __int__(self, pssw):
#         self.pssw = pssw
#
#     def __repr__(self):
#         return f"{self.id} {self.name} {self.pssw} {self.date}"
#
#
#
# Base.metadata.create_all(engine)
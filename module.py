import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
# from flask_sqlalchemy import SQLAlchemy


engine = create_engine('sqlite:///accounts.db')

Base = sqlalchemy.orm.declarative_base()


class Person(Base):
    __tablename__ = "person"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # id = Column(Integer)
    first_name = Column("First Name", String)
    last_name = Column("Last Name", String)
    # personal_id = Column("Personal ID", Integer, unique=True)
    email = Column("Email", String)


    def __repr__(self):
        return f"{self.id}: {self.first_name} {self.last_name}, {self.personal_id}, {self.email}"


class Bank(Base):
    __tablename__ = "bank"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    address = Column("Address", String)
    bank_code = Column("Bank Code", Integer)
    swift_code = Column("SWIFT Code", String)

    def __repr__(self):
        return f"{self.id}: {self.name}, {self.address}, {self.bank_code}, {self.swift_code}"


class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    number = Column("Account Number", Integer)
    balance = Column("Balance", Float)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person")
    bank_id = Column(Integer, ForeignKey('bank.id'))
    bank = relationship("Bank")

    def __repr__(self):
        return f"{self.id}: {self.number}, {self.balance}, {self.person}, {self.bank}"

Base.metadata.create_all(engine)

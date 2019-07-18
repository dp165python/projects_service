from flask import current_app
from sqlalchemy import Column, String, Integer, Float, ForeignKey, create_engine
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Projects(Base):
    __tablename__ = 'projects'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, unique=False, nullable=True)
    contract_id = Column(UUID(as_uuid=True), unique=True, nullable=False)
    status = Column(String, unique=False, nullable=False)
    data = relationship('Data')


class Data(Base):
    __tablename__ = 'data'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey('projects.id'))
    field_1 = Column(Integer)
    field_2 = Column(Integer)
    field_3 = Column(Float)
    field_4 = Column(Integer)
    field_5 = Column(String(80))

from sqlalchemy import Column, Integer, Date, Text
from .Base import Base

class CallTranscription(Base):
    __tablename__ = 'transcribation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    call_date = Column(Date, nullable=False)
    transcribation = Column(Text, nullable=False)

from enum import Enum as Enum_class
from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from dal.base import Base

class Status(Enum_class):
    Active = 1
    Injured = 2
    Missing = 3
    Retired = 4


class Agent(Base):

    __tablename__ = 'agents'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    codeName = Column(String(255), nullable=False, unique=True)
    realName = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    status = Column(SQLEnum(Status), nullable=False)
    missionsCompleted = Column(Integer, nullable=False)
    
    def __new__(cls,  *args, **kwargs):
        # print(f"__ {cls.__name__} created! __")
        return object.__new__(cls)

    def __str__(self) -> str:
        return f"🪪 Agent id: {self.id}\n🧑‍💻 code Name: {self.codeName}\n😊 real Name: {self.realName}\n🏢 location: {self.location}\n🏳️ status: {self.status}\n☢️ missions Completed: {self.missionsCompleted}"
    
    
if __name__ == "__main__":
    pass
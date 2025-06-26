from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker
from dal.base import Base



class DAL:
    
    _instance = None
    
    DB_NAME = "eagleeyedb"
    DB_USER = "root"
    DB_PASSWORD = ""
    DB_HOST = "localhost"
    DB_PORT = "3306"
    
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super(DAL, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.engine = create_engine(f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}",echo=True) # חיבור 
        Base.metadata.create_all(self.engine) #  יצירת טבלה במסד אם לא קיימת 
        self.session = sessionmaker(bind=self.engine)
        
        




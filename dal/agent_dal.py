from models.agent import Agent
from dal.dal import DAL

     

class Agent_dal(DAL):
    
    def __init__(self):
        super().__init__() 
        self.con = None
        
    def create(self, agent: Agent) -> None:
        self.con.add(agent)
        self.con.commit()
    
    def get_all(self) -> list[Agent]:
        return self.con.query(Agent).all()
    
    def get_by_name(self, realName:str) -> list[Agent] | Agent:
        return self.con.query(Agent).filter_by(realName=realName)
    
    def get_by_codeName(self, codeName:str) -> list[Agent] | Agent:
        return self.con.query(Agent).filter_by(codeName=codeName)
    
    def get_by_id(self, agent_id:int) -> Agent:
        return self.con.query(Agent).filter_by(id=agent_id).first()
    
    def delete(self, agent_id:int) -> None:
        agent: Agent = self.con.query(Agent).filter_by(id=agent_id).first()
        if agent:
            self.con.delete(agent)
            self.con.commit()

    def update(self, agent_id:int, dict_agent_update:dict) -> None:
        agent: Agent = self.con.query(Agent).filter_by(id=agent_id).first()
        if agent:
            for key, value in dict_agent_update.items():
                if hasattr(agent, key):
                    setattr(agent, key, value)
            self.con.commit()
    
    def __enter__(self):
        self.con = self.session()
        print("Connection opened")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.con:
            self.con.close()
            print("Connection closed")
    

if __name__ == "__main__":
    pass



from models.agent import Agent, Status
from dal.agent_dal import Agent_dal

class menu:
    
    def __init__(self, dal: Agent_dal):
        self.dal = dal
    
    def start(self):
        while True:
            self.print_menu()

            match input("Select a option: (1-6): "):
                case "1": self.add_agent()
                case "2": self.update_agent()
                case "3": self.get_agent()
                case "4": self.delete_agent()
                case "5": self.get_all_agents()
                case "6": 
                    self.exit()
                    break
                case _ : print("Invalid input! please try again")
                
        
    def add_agent(self):
        name = input("Enter your name: ")
        codeName = self.get_codeName()
        location = input("Enter your location: ")
        status = self.get_status()
        missionsCompleted = input("Enter your missions Completed: ") 
        
        with self.dal as dal:
            agent = Agent(codeName=codeName, realName=name, location=location, status=status, missionsCompleted=missionsCompleted) 
            self.dal.create(agent)
            print("Agent created successfully")
            agent = self.dal.get_by_codeName(codeName)
            print(agent)
    
    def update_agent(self):
        pass
    
    def get_agent(self):
        with self.dal as dal:
            agent = self.dal.get_by_id(self.get_id())
            if agent is None:
                print("Agent not found")
                return
            print(agent)
    
    def delete_agent(self):
        with self.dal as dal:
            agent_id = self.get_id()
            agent = self.dal.get_by_id(agent_id)
            if agent is None:
                print("Agent not found")
                return
            print(agent, " is deleted")
            self.dal.delete(agent_id)
    
    def get_all_agents(self):
        with self.dal as dal:
            for agent in self.dal.get_all():
                print("-----")
                print(agent)
                print("-----")
    
    def exit(self):
        print("\nGoodbye")
        pass
    
    def get_id(self):
        while True:
            match  input("How do you want to select the agent by ID or by codeName?: \n1) id \n2) codeName \n select a option (1 - 2): "):
                case "1":
                    return input("Enter the agent id: ")
                case "2":
                    codeName = input("Enter the agent codeName: ")
                    with self.dal as dal:
                        agent = self.dal.get_by_codeName(codeName)
                        if agent:
                            return agent.id
                        return
                case _:
                    print("Invalid input! please try again")
    
    def get_codeName(self):
        while True:
            codeName = input("Enter your codeName: ")
            with self.dal as dal:
                if self.dal.get_by_codeName(codeName) is None:
                    return codeName
            
            print("Agent already exists with the same codeName please try again")

        
    def get_status(self):
        while True:
            for status in Status:
                print(f"{status.value}) {status.name}")
                
            select = input(F"Select a status: ( 1 - {len(Status)}) ")
            if select.isdigit() and 1 <= int(select) <= len(Status):
                return Status(int(select))
                
            print("Invalid input! please try again")
            
        
    def print_menu(self):
        print()
        print("=" * 10)
        print(" welcome to the menu ")
        print("=" * 10)
        print("1)   Add an agent to the database.")
        print("2)   Update an agent.")
        print("3)   Get an agent.")
        print("4)   Delete an agent.")
        print("5)   Get all agents.")
        print("6)   Exit ")
        print("=" * 10)
        print("What you like to do today?")
        
        
            
if __name__ == "__main__":
    menu(Agent_dal()).start()

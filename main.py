from models.agent import Agent, Status
from dal.agent_dal import Agent_dal
def main():
    print("Hello, world!")
    agent1 = Agent(codeName="Agent 2", realName="John Doe", location="New York", status=Status.Active, missionsCompleted=5)
    
    with Agent_dal() as agent_dal:
        agent_dal.create(agent1)
        print(agent_dal.get_all())
        agent_dal.update(1, {"realName": "Jane Doe", "status": Status.Injured})


if __name__ == "__main__":
    main()

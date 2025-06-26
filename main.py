from menu import menu
from dal.agent_dal import Agent_dal

def main():
    dal = Agent_dal()
    menu(dal).start()


if __name__ == "__main__":
    main()

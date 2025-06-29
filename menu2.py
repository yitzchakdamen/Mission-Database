from models.agent import Agent, Status
from dal.agent_dal import Agent_dal
import streamlit as st

class menu:
    
    def __init__(self, dal: Agent_dal):
        self.dal = dal
    
    def start(self):
        st.title("Agent Management System")

        menu_option = st.sidebar.selectbox(
            "מה אתה רוצה לעשות?",
            ["Add Agent", "Update Agent", "Get Agent", "Delete Agent", "Get All Agents"]
        )

        match menu_option:
            case "Add Agent": self.add_agent()
            case "Update Agent": self.update_agent()
            case "Get Agent": self.get_agent()
            case "Delete Agent": self.delete_agent()
            case "Get All Agents": self.get_all_agents()
            case _: st.write("Invalid input! please try again")

    def add_agent(self):
        with st.form("Add Agent"):
            name = st.text_input("Name")
            codeName = st.text_input("Code Name")
            location = st.text_input("Location")
            status = self.get_status()
            missionsCompleted = st.number_input("Missions", min_value=0, step=1)
            submitted = st.form_submit_button("Create")
            
            if submitted:
                with self.dal as dal:
                    agent = Agent(codeName=codeName, realName=name, location=location,
                                  status=status, missionsCompleted=missionsCompleted)
                    dal.create(agent)
                    st.success("Agent created")

    def update_agent(self):
        st.info("Update agent not implemented yet.")

    def get_agent(self):
        st.subheader("שליפת סוכן")
        agent_id = self.get_id()
        if agent_id and st.button("חפש סוכן"):
            with self.dal as dal:
                agent = dal.get_by_id(agent_id)
                if agent:
                    st.write(agent)
                else:
                    st.error("סוכן לא נמצא")

    def delete_agent(self):
        st.subheader("מחיקת סוכן")
        agent_id = self.get_id()
        if agent_id and st.button("מחק סוכן"):
            with self.dal as dal:
                agent = dal.get_by_id(agent_id)
                if agent:
                    dal.delete(agent_id)
                    st.success("סוכן נמחק בהצלחה")
                else:
                    st.error("סוכן לא נמצא")

    def get_all_agents(self):
        st.subheader("רשימת כל הסוכנים")
        with self.dal as dal:
            agents = dal.get_all()
            for agent in agents:
                st.write("-----")
                st.write(agent)
                st.write("-----")

    def get_id(self):
        st.subheader("בחר איך לזהות את הסוכן")
        method = st.radio("שיטת זיהוי:", ["לפי ID", "לפי codeName"])

        agent_id = None

        if method == "לפי ID":
            id_input = st.text_input("הכנס את ה-ID של הסוכן:")
            if id_input:
                agent_id = id_input

        elif method == "לפי codeName":
            code_input = st.text_input("הכנס את ה-codeName של הסוכן:")
            if code_input:
                with self.dal as dal:
                    agent = dal.get_by_codeName(code_input)
                    if agent:
                        st.success(f"נמצא סוכן: {agent.realName}")
                        agent_id = agent.id
                    else:
                        st.error("סוכן לא נמצא")

        return agent_id

    def get_status(self):
        status_name = st.selectbox("בחר סטטוס מהאפשרויות:", [s.name for s in Status])
        return Status[status_name]

if __name__ == "__main__":
    menu(Agent_dal()).start()

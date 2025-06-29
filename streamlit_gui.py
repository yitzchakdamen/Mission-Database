# import streamlit as st
# from models.agent import Agent, Status
# from dal.agent_dal import Agent_dal

# # אתחול ה-DAL והגדרת משתני session
# if 'dal' not in st.session_state:
#     st.session_state.dal = Agent_dal()

# dal = st.session_state.dal

# st.title("מנוס סוכנים עם Streamlit")

# menu_option = st.sidebar.selectbox(
#     "מה אתה רוצה לעשות?",
#     ["Add Agent", "Update Agent", "Get Agent", "Delete Agent", "Get All Agents"]
# )

# # פונקציה שמחזירה סטטוס לפי בחירה
# def select_status():
#     options = [f"{s.value}) {s.name}" for s in Status]
#     choice = st.selectbox("בחר סטטוס", options)
#     status_index = int(choice.split(")")[0])
#     return Status(status_index)

# # יצירת סוכן
# if menu_option == "Add Agent":
#     with st.form("Add Agent"):
#         name = st.text_input("Enter real name")
#         codeName = st.text_input("Enter code name")
#         location = st.text_input("Enter location")
#         status = select_status()
#         missionsCompleted = st.number_input("Missions completed", min_value=0, step=1)
#         submitted = st.form_submit_button("Create Agent")

#     if submitted:
#         if dal.get_by_codeName(codeName):
#             st.error("Agent already exists with this code name")
#         else:
#             agent = Agent(codeName=codeName, realName=name, location=location,
#                           status=status, missionsCompleted=missionsCompleted)
#             dal.create(agent)
#             st.success("Agent created successfully")
#             st.write(dal.get_by_codeName(codeName))

# # הצגת כל הסוכנים
# elif menu_option == "Get All Agents":
#     agents = dal.get_all()
#     for agent in agents:
#         st.write("-----")
#         st.write(agent)

# # שליפת סוכן
# elif menu_option == "Get Agent":
#     codeName = st.text_input("Enter code name to search")
#     if st.button("Search"):
#         agent = dal.get_by_codeName(codeName)
#         if agent:
#             st.write(agent)
#         else:
#             st.error("Agent not found")

# # מחיקת סוכן
# elif menu_option == "Delete Agent":
#     codeName = st.text_input("Enter code name to delete")
#     if st.button("Delete"):
#         agent = dal.get_by_codeName(codeName)
#         if agent:
#             dal.delete(agent.id)
#             st.success("Agent deleted")
#         else:
#             st.error("Agent not found")

# # עדכון סוכן (פונקציה ריקה במקור)
# elif menu_option == "Update Agent":
#     st.info("Update agent feature is not implemented yet")
